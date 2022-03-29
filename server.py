from dash import Dash, html, dcc, Input, Output
import plotly.graph_objects as go
import random

from GraphInfo import GraphInfo
from ChartInfo import ChartInfo

# 정보 받는 함수
def get_graph_info():
  
  adjList = [ [1, 3, 5, 7],              # 0
              [0],                       # 1
              [],                        # 2
              [5, 7]                     # 3
            ]

  weight = [  [15.1, random.random(), 1.0002, -33],    # 0
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
  return graphInfo

BLACK = 'rgb(0,0,0)'
GRAY = 'rgb(50,50,50)'
AXIS=dict(showbackground=False, showline=False, 
          zeroline=False, showgrid=False, showticklabels=False, 
          title='')

def get_data():
  graphInfo = get_graph_info()
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
                  hoverinfo='none', sizeref=0.1, showscale=False, 
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
        animate=True
    ),
    dcc.Interval(
      id = 'graph-update',
      interval=1000,
      n_intervals=0
    ),
])

@app.callback(
  Output('graph', 'figure'),
  [Input('graph-update', 'n_intervals')]
)
def update(n):
  data = get_data()
  layout = get_layout()
  return go.Figure(data=data, layout=layout)

if __name__ == '__main__':
    app.run_server()