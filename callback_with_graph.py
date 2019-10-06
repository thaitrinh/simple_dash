import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv('gapminderDataFiveYear.csv')

app = dash.Dash()


# https://dash.plot.ly/dash-core-components/dropdown
# We need to construct a dictionary of dropdown values for the years
year_options = []
for year in df['year'].unique():
    year_options.append({'label':str(year),'value':year})

app.layout = html.Div([
    dcc.Graph(id='graph'),
    dcc.Dropdown(id='year-picker',options=year_options,value=df['year'].min())
])

# we want to connect the value of drop down menu to the graph
@app.callback(Output(component_id='graph', component_property='figure'),
              [Input(component_id='year-picker', component_property='value')])

def update_figure(selected_year):
    # selected data
    filtered_df = df[df["year"]==selected_year]

    traces = []
    for continent in filtered_df["continent"].unique():
        df_by_continent = filtered_df[filtered_df["continent"]==continent]
        traces.append(
            go.Scatter(
                x = df_by_continent["gdpPercap"],
                y = df_by_continent["lifeExp"],
                mode="markers",
                opacity=0.7,
                marker={"size":12},
                name=continent
            )
        )
    return {"data":traces,
            "layout":go.Layout(title="My plot",
                               xaxis={"title":"GDP per cap", "type":"log"},
                               yaxis={"title": "Life expectancy"})
            }



if __name__ == "__main__":
    app.run_server()