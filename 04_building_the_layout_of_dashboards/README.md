# Building the layout

The Dash layout is structured as a tree of HTML components. Dash has built-in functions for `h1` to `h6`, `p`, `div`, `br`, `a`, etc. We import the `dash_html_components` module as `html` and then use the HTML elements as

``` python
import dash_html_components as html

html.H1(children = "Hello World")
html.Div(children = html.H1(children = "Hello World"))
```

The first creates an `h1` HTML tag with a child that is just a text that says "Hello World". The second instead, creates a `div`, inside of which it places the `h1` with the "Hello World" text.
