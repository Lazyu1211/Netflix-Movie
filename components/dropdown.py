from dash import Dash, html, dcc
from dash.dependencies import Output,Input
from dash.exceptions import PreventUpdate
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
from utill import get_year, get_year_rate_list

def render(app):
    list_year = get_year()
    all_year = [{'label':i,'value':i} for i in list_year]
    @app.callback(
    Output(component_id='year_dropdown', component_property='value'),
    Input(component_id='select_all_button1', component_property='n_clicks')
    )
    def update_all_year(n):
        return list_year

    return html.Div(
        children=[
            html.H6("Select Years"),
            dcc.Dropdown(
                options=all_year,
                multi=True,
                id = "year_dropdown",
                value= 1
            ),
            dbc.Button(
                children=["Select all"],
                color="primary",
                className="me-1",
                id="select_all_button1",
                n_clicks=0
            )
        ]
    )

def render1(app):
    list_age = get_year_rate_list()
    all_age = [{'label':i,'value':i} for i in list_age]
    @app.callback(
    Output(component_id='age_dropdown', component_property='value'),
    Input(component_id='select_all_button', component_property='n_clicks')
    )
    def update_all_year_rate(n):
        return list_age

    return html.Div(
        children=[
            html.H6("Select Age Limitation"),
            dcc.Dropdown(
                options=all_age,
                multi=True,
                id = "age_dropdown",
                value= 1
            ),
            dbc.Button(
                children=["Select all"],
                color="primary",
                className="me-1",
                id="select_all_button",
                n_clicks=0
            )
        ]
    )
