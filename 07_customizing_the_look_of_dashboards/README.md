# Customization

Since Dash generates web pages, we can add CSS to control the style of the dashboard. You can add CSS inline-declarations to Dash by supplying a dictionary with property names and values to the `style` argument of the component. Keys (property names) must be camelCased. So, `text-align` becomes `textAlign`, and `background-color` becomes `backgroundColor`.

We can add external style sheets by setting the `external_stylesheet` argument in the `Dash` function. To it we pass a list of strings (URLs) or dicts.

We can also user Bootstrap by importing the `dash_bootstrap_components as dbc` module, and passing `dbc.themes.<theme_name>` to the `external_stylesheets` argument of the `Dash` function.
