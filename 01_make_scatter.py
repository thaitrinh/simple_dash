import numpy as np
import plotly.offline as pyo
import plotly.graph_objects as go

np.random.seed(42)

randx = np.random.randint(1, 101, 100)
randy = np.random.randint(1, 101, 100)

# create data for plotting
data = [go.Scatter(x=randx, y=randy, mode="markers")]
# layout
layout = go.Layout(
    title="My scatter plot",
    xaxis={"title":"my x axis"},
    yaxis=dict(title="my y axis"),
    hovermode="closest"
)

fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename="scatter_01.html")
