# Building the layout

The Dash layout is structured as a tree of HTML components. Dash has built-in functions for `h1` to `h6`, `p`, `div`, `br`, `a`, etc. We import the `dash_html_components` module as `html` and then use the HTML elements as

``` python
import dash_html_components as html

html.H1(children = "Hello World")
html.Div(children = html.H1(children = "Hello World"))
```

The first creates an `h1` HTML tag with a child that is just a text that says "Hello World". The second instead, creates a `div`, inside of which it places the `h1` with the "Hello World" text.

We can also use components from the `dash_core_components` module. 

``` python
import dash_core_components as dcc
```

It contains things like `dcc.Dropdown` menus, or `dcc.RadioItems`. I also allows us to add `dcc.Graph` elements where we can use `Plotly`'s Python bindings to include plots and maps into out dashboard. Lastly, it also contains all user facing components such as `dcc.Input` for text input boxes, `dcc.Slder` and `dcc.RangeSlder` for selectors, and much more.

---

The `dcc.RadioItems` element takes two arguments: `options`, and `value`. `options` is usually a list of `dicts` with keys called *label* and *value*. The *label* is what will be displayed on the fron end and the user can interact with. The *value* is the computed value. The second argument is called `value` and it's the default value that will be used when the dashboard is loaded.
