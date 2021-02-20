import dash
import dash_html_components as html
import dash_core_components as dcc
import pandas as pd
import plotly.express as px

HAPPINESS = pd.read_csv("world_happiness.csv")
REGIONS = [{"label": i, "value": i} for i in HAPPINESS["region"].unique()]
COUNTRIES = [{"label": i, "value": i} for i in HAPPINESS["country"].unique()]

line_fig = px.line(
    data_frame=HAPPINESS[HAPPINESS["country"] == "United States"],
    x="year",
    y="happiness_score",
    title="Happiness Score in the USA"
)

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
        dcc.RadioItems(
            options=REGIONS,
            value="North America"  # REGIONS[0]
        ),
        dcc.Checklist(
            options=REGIONS,
            value=["North America"]  # REGIONS[0]
        ),
        dcc.Dropdown(
            options=COUNTRIES,
            value="United States"  # COUNTRIES[0]
        ),
        dcc.Graph(
            figure=line_fig
        )
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)
