from dash import html, dcc, Input, Output, State
import dash_bootstrap_components as dbc
from .utils import with_loading

MODULE_NAME = "tab_03"
def ns(id_):
    return f"{MODULE_NAME}_{id_}"

layout = html.Div([
    dcc.Input(id=ns('input'), value='5', type='text'),
    html.Button('Run', id=ns('btn')),
    html.Div(id=ns('output'))
])

# تابع طولانی
@with_loading
def square_number(x):
    import time
    time.sleep(5)  # شبیه‌سازی پردازش طولانی
    return str(float(x) ** 2)

def register_callbacks(app):
    @app.callback(
        Output(ns('output'), 'children'),
        Output("success-modal", "is_open"),
        Output("long-task-status", "data"),
        Input(ns('btn'), 'n_clicks'),
        State(ns('input'), 'value'),
        State("long-task-status", "data")
    )
    def run_task(n, value, status):
        if not n:
            return "", False, status
        return square_number(value, status)
