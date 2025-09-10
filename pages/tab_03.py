from dash import html, dcc, Input, Output
import dash_admin_components as dac


MODULE_NAME = "tab_03"
def ns(id_):
    return f"{MODULE_NAME}_{id_}"

layout = dac.TabItem(id='layout', 
                              
    children=[
        html.H4('نمونه استفاده از کارت DAC'),
        html.Div([
            dac.ValueBox(
            	value="بخش 3",
                subtitle="زیر بخش 3",
                color = "info",
                icon = "shopping-cart",
                href = "#"
            )
        ], className='row'),
    ]
)

# # sample callback for use 
# def register_callbacks(app):
#     @app.callback(
#         Output(component_id=ns(''), component_property=''),
#         Input(component_id=ns(''),  component_property='')
#     )
#     def update_output(input_data):
#         pass