# Customization

## Inline CSS

Since Dash generates web pages, we can add CSS to control the style of the dashboard. You can add CSS inline-declarations to Dash by supplying a dictionary with property names and values to the `style` argument of the component. Keys (property names) must be camelCased. So, `text-align` becomes `textAlign`, and `background-color` becomes `backgroundColor`.

## External CSS

We can add external style sheets by setting the `external_stylesheet` argument in the `Dash` function. To it we pass a list of strings (URLs) or dicts.

We can also user Bootstrap by importing the `dash_bootstrap_components as dbc` module, and passing `dbc.themes.<theme_name>` to the `external_stylesheets` argument of the `Dash` function.

## Custom CSS

We can also include custom CSS or JavaScript in our Dash apps. We just need to create a folder named `assets` in the root of our app directory and include our CSS and JavaScript files in that folder. Dash will automatically serve all of the files that are included in this folder. By default the URL to request the assets will be `/assets` but we can customize this with the `assets_url_path` argument to `dash.Dash(__name__)` constructor.

## Grid layout

We can use CSS-Grid in Dash. The two main layout components are: 

- `Row`: container for columns

- `Col`: container for content

The layout of the app can be set as a series of rows of columns, with `Col` components as the immediate children of `Row` components.

``` python
dbc.Row([
  dbc.Col(html.Div("Col 1 of 2")),
  dbc.Col(html.Div("Col 2 of 2"))
])
```

``` python
dbc.Row(
  dbc.Col(html.Div("A single column"))
),
dbc.Row([
  dbc.Col(html.Div("Col 1 of 2")),
  dbc.Col(html.Div("Col 2 of 2"))
])
```

If we only want to use grid but specific theme (or a custom one) we need to specify `dash.Dash(external_stylesheets=[dbc.themes.GRID])`.
