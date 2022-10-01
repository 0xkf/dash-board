import dash
import dash_bootstrap_components as dbc
from dash import dcc
from dash import html

import pandas as pd
import numpy as np


df = pd.read_csv('data/data_sample.csv')
vars_cat = [var for var in df.columns if var.startswith('cat')]
vars_cont = [var for var in df.columns if var.startswith('cont')]

app = dash.Dash(external_stylesheets=[dbc.themes.FLATLY])

sidebar = html.Div(
    [
        dbc.Row(
            [
                html.H5('Settings',
                        style={'margin-top': '12px', 'margin-left': '24px'})
                ],
            style={"height": "5vh"},
            className='bg-primary text-white font-italic'
            ),
        dbc.Row(
            [
                html.Div([
                    html.P('Categorical Variable',
                           style={'margin-top': '8px', 'margin-bottom': '4px'},
                           className='font-weight-bold'),
                    dcc.Dropdown(id='my-cat-picker', multi=False, value='cat0',
                                 options=[{'label': x, 'value': x}
                                          for x in vars_cat],
                                 style={'width': '320px'}
                                 ),
                    html.P('Continuous Variable',
                           style={'margin-top': '16px', 'margin-bottom': '4px'},
                           className='font-weight-bold'),
                    dcc.Dropdown(id='my-cont-picker', multi=False, value='cont0',
                                 options=[{'label': x, 'value': x}
                                          for x in vars_cont],
                                 style={'width': '320px'}
                                 ),
                    html.P('Continuous Variables for Correlation Matrix',
                           style={'margin-top': '16px', 'margin-bottom': '4px'},
                           className='font-weight-bold'),
                    dcc.Dropdown(id='my-corr-picker', multi=True,
                                 value=vars_cont + ['target'],
                                 options=[{'label': x, 'value': x}
                                          for x in vars_cont + ['target']],
                                 style={'width': '320px'}
                                 ),
                    html.Button(id='my-button', n_clicks=0, children='apply',
                                style={'margin-top': '16px'},
                                className='bg-dark text-white'),
                    html.Hr()
                    ]
                    )
                ],
            style={'height': '50vh', 'margin': '8px'}),
        dbc.Row(
            [
                html.P('Target Variables', className='font-weight-bold')
                ],
            style={"height": "45vh", 'margin': '8px'}
            )
        ]
    )

content = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.P('Distribution of Categorical Variable',
                               className='font-weight-bold'),
                        ]),
                dbc.Col(
                    [
                        html.P('Distribution of Continuous Variable',
                               className='font-weight-bold')
                    ])
            ],
            style={'height': '50vh',
                   'margin-top': '16px', 'margin-left': '8px',
                   'margin-bottom': '8px', 'margin-right': '8px'}),
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.P('Correlation Matrix Heatmap',
                               className='font-weight-bold')
                    ])
            ],
            style={'height': '50vh', 'margin': '8px'}
            )
        ]
    )

app.layout = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(sidebar, width=3, className='bg-light'),
                dbc.Col(content, width=9)
                ]
            ),
        ],
    fluid=True
    )


if __name__ == "__main__":
    app.run_server(debug=True, port=1234)