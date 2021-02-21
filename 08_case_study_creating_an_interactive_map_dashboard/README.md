# dcc.Graph interactive properties

All Plotly widget have interactive properites. Each one generates its own event that we can capture and use in callback functions:

- `hoverData`: this is event is triggered when the user **hovers over** the Plotly data points or geometries.

- `clickData`: this is event is triggered when the user **clicks**on the Plotly data points or geometries.

- `selectedData`: this is event is triggered when the user **selects a region** of points in the Plotly widget.

- `relayoutData`: this is event is triggered when the user **zooms** in the Plotly widget.

Every event generates a dictionary with its information.
