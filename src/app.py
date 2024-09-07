"""
app.py
- Used for starting the web application.
- This contains the hyperlinks for the various other web pages in `pages` folder.
"""

import dash
from dash import dcc, html
import dash_bootstrap_components as dbc

# Initialize the Dash app
app = dash.Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Main layout with navigation
app.layout = html.Div(
    [
        dcc.Location(id="url", refresh=False),
        html.Div(
            [
                html.Div(
                    [
                        dcc.Link("Home", href="/", className="nav-link"),
                        dcc.Link(
                            "Detect", href="/detect", className="nav-link"
                        ),
                    ],
                    className="nav",
                ),
                html.Div(id="page-content", className="container"),
            ]
        ),
        dash.page_container,
    ]
)


