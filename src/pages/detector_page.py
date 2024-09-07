"""
Detector Page for the Web Application.
This is where the Videos are uploaded and detect
"""

import dash
from dash import html, dcc, Input, Output, State
import dash_bootstrap_components as dbc

# Register the page for multi-page support
dash.register_page(__name__, path="/detect")

# Layout with a title, upload component, and a detect button
layout = html.Div([
    html.H1("Detect", className = "title-text"),  # Title
    
    # Upload component for uploading files
    dcc.Upload(
        id='upload-data',
        children=html.Div([
            'Drag and Drop or ', html.A('Select Files')
        ]),
        # style={
        #     'width': '100%',
        #     'height': '60px',
        #     'lineHeight': '60px',
        #     'borderWidth': '1px',
        #     'borderStyle': 'dashed',
        #     'borderRadius': '5px',
        #     'textAlign': 'center',
        #     'margin': '10px'
        # },
        className = "upload-container",
        multiple=False,  # Allow only a single file
    ),
    
    # Detect button
    dbc.Button("Detect", id='detect-button', color="primary", n_clicks=0),
    
    # Display uploaded file information
    html.Div(id='output-upload'),
    
    # Display detection result
    html.Div(id='output-detect'),
])



# Callback for uploading content
@dash.callback(
    Output('output-upload', 'children'),
    Input('upload-data', 'contents'),
    State('upload-data', 'filename'),
    prevent_initial_call = True
)
def upload_content(contents, filename):
    if contents is not None:
        return html.Div([
            html.H5(f"Uploaded file: {filename}"),
            html.P("Upload successful.")
        ])
    return html.Div("Please upload a file.")

# Callback for detect button
@dash.callback(
    Output('output-detect', 'children'),
    Input('detect-button', 'n_clicks'),
    State('upload-data', 'contents'),
    prevent_initial_call = True

)
def detect_button(n_clicks, contents):
    if n_clicks > 0:
        if contents is None:
            return "No file uploaded. Please upload a file first."
        return "Detect button clicked! Processing the uploaded file..."
    return ""



