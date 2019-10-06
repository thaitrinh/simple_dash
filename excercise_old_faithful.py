import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.offline as pyo
import plotly.graph_objects as go


df = pd.read_csv("OldFaithful.csv")

data = [go.Scatter(x=df["X"],
                   y=df["Y"],
                   mode="markers",
                   marker={"size":12, "color":"rgb(51, 204, 153)"})
]
layout = go.Layout(title="Old Faithful scatter",
                   xaxis={"title":"eruption duration"},
                   yaxis={"title":"waiting time"})

app = dash.Dash()

app.layout = html.Div(
    [dcc.Graph(
        id="old_faithful",
        figure={
            "data":data,
            "layout":layout
        }
    )]
)

if __name__ == "__main__":
    app.run_server()


