import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash()

app.layout = html.Div([
    dcc.Input(id="my_input", value="initial text", type="text"),
    html.Div(id="my_output")
])

# a decorator is used to connect input and output
@app.callback(Output(component_id="my_output", component_property="children"),
              [Input(component_id="my_input", component_property="value")])

def update_output_div(input_val):
    return "You entered: {}".format(input_val)


if __name__ == "__main__":
    app.run_server()