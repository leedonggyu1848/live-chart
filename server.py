from dash import Dash, html, dcc, Input, Output
import plotly.graph_objects as go
from random_graph import random_graph

from GraphInfo import GraphInfo
from ChartInfo import ChartInfo

import configparser

config = configparser.ConfigParser()
config.read('config.ini')
N_NODE = int(config['GRAPH']['node'])
N_EDGE = int(config['GRAPH']['edge'])

BLACK = 'rgb(0,0,0)'
GRAY = 'rgb(50,50,50)'
AXIS=dict(showbackground=False, showline=False, 
          zeroline=False, showgrid=False, showticklabels=False, 
          title='')

def get_data():
  graphInfo = random_graph(N_NODE, N_EDGE)
  chartInfo = ChartInfo(GraphInfo(**graphInfo))
  e_trace=go.Scatter3d(mode='lines',
                      line=dict(color=BLACK, width=1),
                      hoverinfo='none', **chartInfo.get_edges())

  n_trace=go.Scatter3d(mode='markers', name='actors', 
                      marker=dict(symbol='circle', size=6, 
                      colorscale='Viridis', 
                      line=dict(color=GRAY, width=0.5)), 
                      hoverinfo='text', **chartInfo.get_nodes())

  t_trace=go.Scatter3d(mode='text', textposition='top center', 
                      hoverinfo='none', **chartInfo.get_texts())

  d_trace=go.Cone(anchor='tip', sizemode="absolute", 
                  hoverinfo='none', sizeref=0.05, showscale=False, 
                  colorscale=[[0, BLACK], [1,BLACK]], 
                  **chartInfo.get_cones())
                  
  return [n_trace, e_trace, t_trace, d_trace]

def get_layout():
  layout = go.Layout(
         title="Network",
         width=1000,
         height=1000,
         showlegend=False,
         scene=dict(
             xaxis=dict(AXIS),
             yaxis=dict(AXIS),
             zaxis=dict(AXIS),
        ))
  return layout

app = Dash(__name__)

app.layout = html.Div(children=[
    dcc.Graph(
        id='graph',
        figure=go.Figure(data=get_data(), layout=get_layout()),
    ),
    dcc.Interval(
      id = 'graph-update',
      interval=2000,
      n_intervals=0
    ),
])

# @app.callback(
#   Output('graph', 'figure'),
#   [Input('graph-update', 'n_intervals')]
# )
# def update(n):
#   data = get_data()
#   layout = get_layout()
#   return {'data':data, 'layout':layout}

if __name__ == '__main__':
    app.run_server()