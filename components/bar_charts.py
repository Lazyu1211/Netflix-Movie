from dash import Dash, html, dcc
from dash.dependencies import Output,Input
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
from utill import get_year_count, get_year_rate, get_sub, get_audio

def render(app):
    df = get_year_count()

    @app.callback(
        Output("bar_volume", component_property='children'),
        Input("year_dropdown",component_property='value')
    )

    def update_bar_chart(dropdown):
        filtered_data = df.query("year in @dropdown")
        fig = px.bar(
                filtered_data,
                x="year",
                y="release movies count",
                color="release movies count",
                title="Release Year Count")
        return html.Div(dcc.Graph(figure=fig),id="bar_volume")
    return html.Div(id="bar_volume")

def render1(app):
    df = get_year_rate()

    @app.callback(
        Output("bar_volume1", component_property='children'),
        Input("age_dropdown",component_property='value')
    )

    def update_bar_chart(dropdown):
        filtered_data = df.query("age_limitation in @dropdown")
        fig = px.bar(
                filtered_data,
                x="age_limitation",
                y="maturity_rating",
                color="maturity_rating",
                title="Age Limitation")
        return html.Div(dcc.Graph(figure=fig),id="bar_volume1")
    return html.Div(id="bar_volume1")

def render2(app):
    df = get_sub()
    fig = px.bar(df, x="subtitle_classification", y="subtitles", color="subtitles", title="Subtitle Classification")
    return html.Div(dcc.Graph(figure=fig),id="bar_volume2")

def render3(app):
    df = get_audio()
    fig = px.bar(df, x=df.index, y="audio", color="audio", title="Audio Classification")
    return html.Div(dcc.Graph(figure=fig),id="bar_volume3")