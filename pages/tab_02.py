from dash import html, dcc, Input, Output
import dash_admin_components as dac

MODULE_NAME = "tab_02"
def ns(id_):
    return f"{MODULE_NAME}_{id_}"

layout = html.Div([
    dcc.Input(id=ns('input'), value=f'Enter a number: {ns('input')}', type='text'),
    html.Div(id=ns('output'))
])

def register_callbacks(app):
    @app.callback(
        Output(ns('output'), 'children'),
        Input(ns('input'), 'value')
    )
    def update_output(input_data):
        try:
            return str(float(input_data) ** 2)
        except:
            return "Error, the input is not a number"
