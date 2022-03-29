from dash import Dash, html, dcc, Input, Output, State
import plotly.express as px
import pandas as pd

import numpy as np
import networkx as nx
import igraph as ig

import plotly.graph_objects as go
from plotly.offline import iplot
import chart_studio.plotly as py

from collections import OrderedDict

from GraphInfo import GraphInfo
from ChartInfo import ChartInfo

adjList = [ [1, 3, 5, 7],              # 0
            [0],                       # 1
            [],                        # 2
            [5, 7]                     # 3
           ]

weight = [  [15.1, 10, 1.0002, -33],    # 0
            [-32.7],                    # 1
            [],                         # 2
            [-1, 0]                     # 3
          ]

nodeValue = [ -0.1,                         # 0
              14,                           # 1
              10,                           # 2
              0,                            # 3
            ]

graphInfo = {
    'adjList' : adjList,
    'weight' : weight,
    'nodeValue' : nodeValue,
}

chartInfo = ChartInfo(GraphInfo(**graphInfo))
line_color = 'rgb(0,0,0)'
marker_color = 'rgb(50,50,50)'
e_trace=go.Scatter3d(mode='lines',
                    line=dict(color=line_color, width=1),hoverinfo='none', **chartInfo.get_edges())

n_trace=go.Scatter3d(mode='markers', name='actors', 
                    marker=dict(symbol='circle', size=6, colorscale='Viridis', 
                    line=dict(color=marker_color, width=0.5)), hoverinfo='text', **chartInfo.get_nodes())

t_trace=go.Scatter3d(mode='text', textposition='top center', hoverinfo='none', **chartInfo.get_texts())

d_trace=go.Cone(anchor='tip', sizemode="absolute", hoverinfo='none', sizeref=0.1, showscale=False, colorscale=[[0, line_color], [1,line_color]], **chartInfo.get_cones())

axis=dict(showbackground=False, showline=False, zeroline=False, showgrid=False, showticklabels=False, title='')
layout = go.Layout(
         title="Network",
         width=1000,
         height=1000,
         showlegend=False,
         scene=dict(
             xaxis=dict(axis),
             yaxis=dict(axis),
             zaxis=dict(axis),
        ))
data=[n_trace, e_trace, t_trace, d_trace]

fig=go.Figure(data=data, layout=layout)

app = Dash(__name__)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options


app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),
    
    dcc.Input(id="data"),

    html.Button(id='button', children='submit', n_clicks=0),

    dcc.Graph(
        id='graph',
        figure=fig
    ),

])


@app.callback(
  Output('graph', 'figure'),
  Input('button', 'n_clicks'),
  State('data', 'value')
)
def update(n_clicks, value):
  data=[n_trace, e_trace, t_trace, d_trace]
  fig=go.Figure(data=data, layout=layout)
  return fig

if __name__ == '__main__':
    app.run_server()