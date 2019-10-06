import dash
import dash_core_components as dcc
import dash_html_components as html


app = dash.Dash()

app.layout = html.Div([html.H1("Show some core components"),
                       # Dropdown
                       html.Label("Drop down menu"),
                       dcc.Dropdown(options=[{"label":"New York City",
                                             "value":"NYC"},
                                             {"label":"San Francisco",
                                             "value":"SF"},
                                             ],
                                    value="SF"      # default value
                                    ),
                       # Slider
                       html.Label("Slider"),
                       dcc.Slider(min=-10, max=10, step=0.5, value=0,
                                  marks={i:i for i in range(-10, 11, 1)}),
                       # Radio items
                       html.P(html.Label("Radio items")),
                       dcc.RadioItems(options=[{"label":"New York City",
                                                "value":"NYC"},
                                               {"label":"San Francisco",
                                                "value":"SF"},
                                               ],
                                      value="SF"
                                      )
                       ])


if __name__ == "__main__":
    app.run_server()