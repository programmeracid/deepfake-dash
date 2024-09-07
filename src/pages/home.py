"""
First Landing Page for the Web Application.
Temporarily Empty
"""

import dash
from dash import html

dash.register_page(__name__, path="/")

layout = html.Div([html.H1("Home Page"), html.P("Head on to Visualize and start visualizing data from InfluxDB")],
                  style = {
                      "text-align" : "center",
                      "display" : "flex",
                      "justify-content" : "center",
                      "flex-direction" : "column",
                  })
