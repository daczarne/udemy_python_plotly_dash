import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

HAPPINESS = pd.read_csv("world_happiness.csv")
COUNTRIES = [{"label": i, "value": i} for i in HAPPINESS["country"].unique()]

app = dash.Dash()

app.layout = html.Div(
    children=[
        html.H1(
            children="World Happiness Dashboard"
        ),
        html.P(
            children=[
                "This dashboard shows the happiness score",
                html.Br(),
                html.A(
                    children="World Happiness report data source",
                    href="https://worldhappiness.report/",
                    target="_blank"
                )
            ]
        ),
        dcc.Dropdown(
            id="country-dropdown",
            options=COUNTRIES,
            value="United States"  # COUNTRIES[0]
        ),
        dcc.RadioItems(
            id="data-radio",
            options=[
                {"label": "Happiness Score", "value": "happiness_score"},
                {"label": "Happiness Rank", "value": "happiness_rank"}
            ],
            value="happiness_score"
        ),
        dcc.Graph(
            id="happiness-plot"
        )
    ]
)


@app.callback(
    Output(component_id="happiness-plot", component_property="figure"),
    Input(component_id="country-dropdown", component_property="value"),
    Input(component_id="data-radio", component_property="value")
)
def update_plot(selected_country, selected_data):
    # Filter the data
    filtered_happiness = HAPPINESS[HAPPINESS["country"] == selected_country]

    # Build the plot
    line_fig = px.line(
        data_frame=filtered_happiness,
        x="year",
        y=selected_data,
        title=f"{selected_data} for {selected_country}"
    )

    # Return the plot
    return line_fig


if __name__ == "__main__":
    app.run_server(debug=True)
