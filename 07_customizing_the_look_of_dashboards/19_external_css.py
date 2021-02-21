import dash
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import pandas as pd

# Global variables
PLAYERS = pd.read_csv("fifa_football_players.csv")
PLAYER_NAME = [{"label": i, "value": i} for i in PLAYERS["long_name"].unique()]

# Instaciate
app = dash.Dash(external_stylesheets=[dbc.themes.CYBORG])

# Build layour
app.layout = html.Div([
    html.H1("Football players dashboard"),
    html.P([
        "Source: ",
        html.A(
            "Sofifa",
            href="https:://sofifa.com/",
            target="_blank"
        )
    ]),
    html.Label("Player name: "),
    dcc.Dropdown(
        options=PLAYER_NAME,
        value=PLAYER_NAME[0]["value"]
    )
])

if __name__ == "__main__":
    app.run_server(debug=True)
