from dash import Dash,html
import os   
import dash_bootstrap_components as dbc
from components import dropdown, bar_charts, pie_charts

image_path = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT7u_dWAfX60VjjZmHYVuzO_2cAcaR2_0dR8w&usqp=CAU"
image_path1 = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRvxUBnHl0QMklU-uU30wFo6Z0Tz6WNMTou4w&usqp=CAU"

def create_layout(app):
    return dbc.Container(children=[
        dbc.Row([
        html.H1(
                "Netflix Movies Analysis", className="header-title", style={'margin-top': '10px', 'text-align': 'center'}
              ),
        html.P(
                "Base on the dataset we can analysis the Netflix Movies with over two hours duration between 2020 and 2023!!!🔥🔥🔥🍿🍿🍿💫💫💫",
                className="header-description", style={'margin-top': '10px', 'text-align': 'center'}
                ),
        html.P(children="✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨", className="header-emoji", style={'margin-top': '10px', 'text-align': 'left'}),
        html.Img(src=image_path, style={"width": "660px", "height": "400px"}),
        html.Img(src=image_path1, style={"width": "660px", "height": "400px"}),
        html.P(children="✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨", className="header-emoji", style={'margin-top': '10px', 'text-align': 'left'}),
        dbc.Col(dropdown.render(app),style={'margin-top': '30px', 'text-align': 'left'}),
        dbc.Col(dropdown.render1(app),style={'margin-top': '30px', 'text-align': 'left'})
,       
    ],className="mt-4"),
        dbc.Row([
            dbc.Col(bar_charts.render(app),lg=6,style={'margin-top': '20px'}),
            dbc.Col(bar_charts.render1(app),lg=6,style={'margin-top': '20px'}),
            dbc.Col(pie_charts.render(app),lg=6,style={'margin-top': '50px', 'text-align': 'center'}),
            dbc.Col(bar_charts.render2(app),lg=6,style={'margin-top': '50px', 'text-align': 'center'}),
            dbc.Col(
    html.P("Specific genres and audio classification, please see the attached Image in Components Folder!!!📂📂📂"),
    lg=12,
    style={'margin-top': '50px', 'text-align': 'center'}
),
            dbc.Col(pie_charts.render1(app),lg=6,style={'margin-top': '20px', 'text-align': 'center'}),
            dbc.Col(bar_charts.render3(app),lg=6,style={'margin-top': '20px', 'text-align': 'center'})
        ],className="mt-4"),
    ])
