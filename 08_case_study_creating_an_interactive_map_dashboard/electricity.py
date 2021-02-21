import dash
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import dash_table
import pandas as pd
import plotly.express as px

# Global variables
ELECTRICITY = pd.read_csv("electricity.csv")
MIN_YEAR = ELECTRICITY["Year"].min()
MAX_YEAR = ELECTRICITY["Year"].max()

# Instanciate app
app = dash.Dash(external_stylesheets=[dbc.themes.SOLAR])

# Define layout
app.layout = html.Div([
    html.H1("Electricity prices by US state"),
    dcc.RangeSlider(
      id = "year-slider",
      min = MIN_YEAR,
      max = MAX_YEAR,
      value = [MIN_YEAR, MAX_YEAR],
      marks = {i: str(i) for i in range(MIN_YEAR, MAX_YEAR + 1)}
    ),
    dcc.Graph(
      id = "map-graph"
    ),
    #html.Div(id = "click-children"),
    dash_table.DataTable(
      id = "price-info",
      columns = [{"name": col, "id": col} for col in ELECTRICITY.columns]
    )
])

# Callback for range selector
@app.callback(
  Output(component_id = "map-graph", component_property = "figure"),
  Input(component_id = "year-slider", component_property = "value"),
)
def update_map_graph(selected_years):
  # Filter the data
  filtered_electricity = ELECTRICITY[
      (ELECTRICITY["Year"] >= selected_years[0])
      & (ELECTRICITY["Year"] <= selected_years[1])
  ]
  # Compute the avg
  avg_price_electricity = filtered_electricity.groupby("US_State")["Residential Price"].mean().reset_index()
  # Build the map
  map_fig = px.choropleth(
      avg_price_electricity,
      locations = "US_State",
      locationmode = "USA-states",
      color = "Residential Price",
      scope = "usa",
      color_continuous_scale = "reds"
  )
  # Return the map
  return map_fig


# Callback for map clicking
@app.callback(
  Output(component_id = "price-info", component_property = "data"),
  Input(component_id = "map-graph", component_property = "clickData"),
  Input(component_id = "year-slider", component_property = "value")
)
# def print_clicked_data(clicked_data):
#  return str(clicked_data)
def update_data_table(clicked_data, selected_years):
  if clicked_data is None:
    return []
  # Get the clicked data
  us_state = clicked_data["points"][0]["location"]
  # Created new data frame filtered US
  filtered_electricity = ELECTRICITY[
    (ELECTRICITY["US_State"] == us_state)
    & (ELECTRICITY["Year"] >= selected_years[0])
    & (ELECTRICITY["Year"] <= selected_years[1])
  ]
  # Return the output as dicts
  return filtered_electricity.to_dict("records")


# Run app
if __name__ == "__main__":
    app.run_server(debug = True)
