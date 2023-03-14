from dash import Dash, html, dcc
import plotly.express as px
from dash.dependencies import Output,Input
from utill import get_mood, get_genre

def render(app):
    df = get_mood()
    fig = px.pie(df, values = "mood", names =df.index, title="Movie Mood Classification")
    return html.Div(dcc.Graph(figure=fig),id="pie_chart")

def render1(app):
    df = get_genre()
    fig = px.pie(df, values = "genre", names =df.index, title="Movie Genre Classification")
    return html.Div(dcc.Graph(figure=fig),id="pie_chart1")
