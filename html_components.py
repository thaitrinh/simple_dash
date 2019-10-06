import dash
import dash_html_components as html
import dash_core_components as dcc

app = dash.Dash()

# app.layout = html.H1("Hello")
# app.layout = html.Div(html.H1("Hello"))
app.layout = html.Div(["This is the mos outer div",
                       html.Div(["This is an inner div"],
                                style={"color":"red", "border":"2px red solid"}),
                       html.Div("This is another inner div",
                                style={"color":"blue", "border":"2px blue solid"}),
                       ],
                      style={"color":"green", "border":"2px green solid"})

if __name__ == "__main__":
    app.run_server()