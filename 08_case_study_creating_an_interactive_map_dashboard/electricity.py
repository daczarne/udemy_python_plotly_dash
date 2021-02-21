import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import pandas as pd

# Global variables
ELECTRICITY = pd.read_csv("electricity.csv")
MIN_YEAR = ELECTRICITY["Year"].min()
MAX_YEAR = ELECTRICITY["Year"].max()

# Instanciate app
app = dash.Dash()

# Define layout
app.layout = html.Div([
    html.H1("Electricity prices by US state"),
    dcc.RangeSlider(
        id="year-slider",
        min=MIN_YEAR,
        max=MAX_YEAR,
        value=[MIN_YEAR, MAX_YEAR],
        marks={i: str(i) for i in range(MIN_YEAR, MAX_YEAR + 1)}
    )
])

# Callbacks


# Run app
if __name__ == "__main__":
    app.run_server(debug=True)
