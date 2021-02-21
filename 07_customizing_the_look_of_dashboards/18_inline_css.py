import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

# Global variables
PLAYERS = pd.read_csv("fifa_football_players.csv")
PLAYER_NAME = [{"label": i, "value": i} for i in PLAYERS["long_name"].unique()]

# Instaciate
app = dash.Dash()

# Build layour
app.layout = html.Div(
    children=[
        html.H1(
            "Football players dashboard",
            style={
                "textAlign": "center",
                "fontFamily": "fantasy",
                "fontSize": "50px",
                "color": "blue"
            }
        ),
        html.P(
            children=[
                "Source: ",
                html.A(
                    "Sofifa",
                    href="https:://sofifa.com/",
                    target="_blank"
                )
            ],
            style={
                "border": "solid"
            },
        ),
        html.Label("Player name: "),
        dcc.Dropdown(
            options=PLAYER_NAME,
            value=PLAYER_NAME[0]["value"],
            style={
                "backgroundColor": "lightblue"
            }
        )
    ],
    style={
        "padding": "100px",
        "border": "solid"
    }
)

if __name__ == "__main__":
    app.run_server(debug=True)
