import numpy as np
import plotly.offline as pyo
import plotly.graph_objects as go
import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

# create data
np.random.seed(42)
randx = np.random.randint(1, 101, 100)
randy = np.random.randint(1, 101, 100)
# graphic elements
trace0 = go.Scatter(x=randx, y=randy, mode="markers",
                   marker={"size":15,
                           "color":"rgb(51, 204, 153)"})

trace1 = go.Scatter(x=randx, y=randy, mode="markers",
                   marker={"size":15,
                           "color":"rgb(204, 51, 153)"})

data0 = [trace0]
data1 = [trace1]

layout = go.Layout(title="My scatter plot",
                   xaxis={"title":"x label"},
                   yaxis={"title":"y label"})

app.layout = html.Div([
    dcc.Graph(id="scatter_plt",
              figure={"data":data0, "layout":layout}),
    dcc.Graph(id="second_plt",
              figure={"data": data1, "layout": layout})
    ]
)

if __name__ == "__main__":
    app.run_server()
