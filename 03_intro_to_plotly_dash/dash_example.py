from logging import debug
import dash
import dash_html_components as html

# Instanciate an app
app = dash.Dash()

# Declare the layout
app.layout = html.Div("Hello, world!")

if __name__ == "__main__":
    app.run_server(debug=True)
