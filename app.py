import dash
from dash import html, dcc, Input, Output
import dash_bootstrap_components as dbc
import importlib
import os
import types

# Dash
app = dash.Dash(
    __name__,
    suppress_callback_exceptions=True,
    external_stylesheets=[
        "/assets/css/bootstrap.rtl.min.css",
        "/assets/css/all.min.css",
        "/assets/custom.css"
    ]
)
app.title = "داشبورد "

# load pages (import) and call callback decorator for any app
PAGES_DIR = "pages"
pages = {}
for file in os.listdir(PAGES_DIR):
    if file.endswith(".py") and file != "__init__.py":
        module_name = file[:-3]  # فقط نام فایل بدون پسوند
        full_module_name = f"{PAGES_DIR}.{module_name}"
        module = importlib.import_module(full_module_name)

        # فرض بر این است که layout در ماژول تعریف شده
        pages["/" + module_name] = module.layout

        # اگر تابع register_callbacks وجود دارد، آن را صدا بزن
        if hasattr(module, "register_callbacks"):
            module.register_callbacks(app)



# Sidebar items
sidebar_items = [
    {"id": "tab_01", "label": "تب اول", "icon": "fa fa-home"},
    {"id": "tab_02", "label": "تب دوم", "icon": "fa fa-chart-line"},
    {"id": "tab_03", "label": "تب سوم", "icon": "fa fa-file-alt"},
    {"id": "tab_04", "label": "تب چهارم", "icon": "fa fa-users"},
    {"id": "tab_05", "label": "تب پنجم", "icon": "fa fa-calculator"}
]

# Layout
app.layout = html.Div([
    dcc.Location(id="url", refresh=False),

    # Navbar
    dbc.Navbar(
        children=[
            dbc.Button(
                html.I(className="fa fa-bars"),
                id="btn_sidebar",
                color="secondary",
                className="m-2"
            ),
            dbc.NavbarBrand("داشبورد آزمایشگاه علم داده ", className="me-auto"),
            dbc.Nav(
                [
                    dbc.NavItem(html.I(className="fa fa-user mt-3")),
                    dbc.NavItem(dbc.NavLink("جهت استفاده لوکال", href="#")),
                    
                ],
                className="m-2",
                navbar=True
            )
        ],
        color="dark",
        fixed="top"
    ),

    # Sidebar
    html.Div(
        id="sidebar",
        children=[
            html.Div(
                [html.I(className=item["icon"]), html.Span(item["label"], className="ms-2")],
                id=item["id"],
                className="sidebar-item"
            )
            for item in sidebar_items
        ]
    ),

    # Page content
    html.Div(id="page-content",)
])

# Toggle Sidebar
@app.callback(
    Output("sidebar", "className"),
    Output("page-content", "style"),
    Input("btn_sidebar", "n_clicks"),
    [dash.dependencies.State("sidebar", "className")]
)
def toggle_sidebar(n, current_class):
    if not current_class:
        current_class = ""
    collapsed = "collapsed" not in current_class if n else "collapsed" in current_class
    class_name = "collapsed" if collapsed else ""
    style = {"marginRight": "80px" if collapsed else "250px", "transition": "margin 0.3s", "paddingTop": "70px"}
    return class_name, style


@app.callback(
    Output("page-content", "children"),
    [Input(item["id"], "n_clicks") for item in sidebar_items]
)
def display_page(*args):
    ctx = dash.callback_context
    if not ctx.triggered:
        return pages.get("/tab_01")
    button_id = ctx.triggered[0]["prop_id"].split(".")[0]
    return {
        "tab_01": pages.get("/tab_01"),
        "tab_02": pages.get("/tab_02"),
        "tab_03": pages.get("/tab_03"),
        "tab_04": pages.get("/tab_04"),
        "tab_05": pages.get("/tab_05")
    }.get(button_id, pages.get("/tab_01"))


if __name__ == "__main__":
    app.run(debug=True)
