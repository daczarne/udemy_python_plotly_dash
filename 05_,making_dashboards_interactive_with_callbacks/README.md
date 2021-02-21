# Callbacks

Callback functions are Python functions and can thus be defined as such. The main difference is that they are **decorated** functions. This funtions will be automatically called by Python when an input's component property changes. Their goal is to update an output component.

!["callbacks](callbacks.png)

To use callback functions we need to import the `Input` and `Output` objects from the `dash.dependencies` module. The general syntax of a callback function is as follows:

``` python
# Function decorator (Outputs first)
@app.callback(
  Output(component_id, component_property),
  Input(component_id, component_property)
)
# Function
def function_name(input_argument_name):
  # Function body
  return output_object
```

Before using a component in a callback function we need to declare it in the app layout. We need to give it a unique name (its ID).

!["input and output"](input-output.png)
