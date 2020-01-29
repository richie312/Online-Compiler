# -*- coding: utf-8 -*-

import os
import flask
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go
from log_analysis import dataframe_plot

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

""" read the logfile"""
    
with open(r'nohup.out','r',encoding='cp850') as readfile:
    logfile = readfile.readlines()
    
df_ebola = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2014_ebola.csv')
df_ebola = df_ebola.dropna(axis=0)

df_dict = dataframe_plot(logfile)
server = flask.Flask(__name__)
app = dash.Dash(__name__, server=server,suppress_callback_exceptions=True)

def app_layout():
    return(
            html.Div([
        html.Div([html.H1("Skillz Api Performance - 2019")], style={"textAlign": "center"}),
        dcc.Graph(id="my-graph"),dcc.Graph(id = "my-ebola-graph"),
        html.Div([dcc.Slider(id='month-selected', min=3, max=12, value=8,
                             marks={3: "March", 4: "April", 5: "May", 6: "June", 7: "July", 8: "August", 9: "September",
                                    10: "October", 11: "November", 12: "December"})],
                 style={'textAlign': "center", "margin": "30px", "padding": "10px", "width": "65%", "margin-left": "auto",
                        "margin-right": "auto"}),
    ], className="container")
    )

app.layout=app_layout()

@app.callback(
    dash.dependencies.Output("my-graph", "figure"),
    [dash.dependencies.Input("month-selected", "value")]
)
def update_graph(selected):
    return {
        "data": [go.Pie(labels=df_dict['success']['API'].values.tolist(), values=df_dict['success'][df_dict['success']['Month'] == selected]['Group_Count'].values.tolist(),
                        marker={'colors': ['#EF963B', '#C93277', '#349600', '#EF533B', '#57D4F1']}, textinfo='label')],
        "layout": go.Layout(title="Count of Error Code:200 of Each API", margin={"l": 300, "r": 300, },
                            legend={"x": 1, "y": 0.7})}
@app.callback(
dash.dependencies.Output("my-ebola-graph", "figure"),
[dash.dependencies.Input("month-selected", "value")]
)
    
def update_ebola_graph(selected):
    return {
        "data": [go.Pie(labels=df_ebola["Country"].unique().tolist(), values=df_ebola[df_ebola["Month"] == selected]["Value"].tolist(),
                        marker={'colors': ['#EF963B', '#C93277', '#349600', '#EF533B', '#57D4F1']}, textinfo='label')],
        "layout": go.Layout(title="Cases Reported Monthly", margin={"l": 300, "r": 300, },
                            legend={"x": 1, "y": 0.7})}

        
if __name__ == '__main__':
    app.server.run(host = '0.0.0.0',port = 5002,debug = True)