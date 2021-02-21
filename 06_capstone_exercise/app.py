from logging import debug
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

# Global variables
AVOCADO = pd.read_csv("avocado.csv")
GEOGRAPHY = [{"label": i, "value": i} for i in AVOCADO["geography"].unique()]

# Instatiates app
app = dash.Dash()

# Defines layout
app.layout = html.Div([
    html.H1("Avocado Prices Dashboard"),
    dcc.Dropdown(
        id="geo-dropdown",
        options=GEOGRAPHY,
        value="New York"
    ),
    dcc.Graph(
        id="price-graph"
    )
])


@app.callback(
    Output(
        component_id="price-graph",
        component_property="figure"
    ),
    Input(
        component_id="geo-dropdown",
        component_property="value"
    )
)
def update_plot(selected_geo):
    # Filter data for the selected geo
    filtered_df = AVOCADO[AVOCADO["geography"] == selected_geo]
    # Build plot
    fig = px.line(
        filtered_df,
        x="date",
        y="average_price",
        color="type",
        title=f"Avg. price of avocados in {selected_geo}"
    )
    # Return the plot
    return fig


if __name__ == "__main__":
    app.run_server(debug=True)
