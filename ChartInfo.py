from helper import *

class ChartInfo:
  def __init__(self, graphInfo):
    import igraph as ig
    self.__graphInfo = graphInfo
    G = ig.Graph(directed=True)
    G.add_vertices(graphInfo.get_vertices())
    G.add_edges(graphInfo.get_edges())
    self.__layt = G.layout('kk', dim=3)

  def get_node_labels(self):
    format = 'node'
    return [f'node: {ver} value: {safe_list_get(self.__graphInfo.get_node_value(), ver)}'
            for ver in range(self.__graphInfo.get_vertices())]
  
  def get_edge_labels(self):
    labels=[]
    for y, weights in enumerate(self.__graphInfo.get_weight()):
      for x, weight in enumerate(weights):
        s, e = y, self.__graphInfo.get_adjlist()[y][x]
        labels.append(f'{s}->{e}: {weight}')
    return labels

  def get_nodes(self):
    xn=[]
    yn=[]
    zn=[]
    layt = self.__layt
    for k in range(self.__graphInfo.get_vertices()):
      xn.append(layt[k][0])
      yn.append(layt[k][1])
      zn.append(layt[k][2])
    return {
        'x':xn,
        'y':yn,
        'z':zn,
        'text': self.get_node_labels()
    }
  
  def get_edges(self):
    xe=[]
    ye=[]
    ze=[]
    layt = self.__layt

    for e in self.__graphInfo.get_edges():
      xe+=[layt[e[0]][0],layt[e[1]][0],None]
      ye+=[layt[e[0]][1],layt[e[1]][1],None]
      ze+=[layt[e[0]][2],layt[e[1]][2],None]
    
    return {
        'x':xe,
        'y':ye,
        'z':ze
    }

  def get_cones(self):
    layt = self.__layt
    xd=[]
    yd=[]
    zd=[]
    ud=[]
    vd=[]
    wd=[]

    for e in self.__graphInfo.get_edges():  
      xd.append(layt[e[1]][0])
      yd.append(layt[e[1]][1])
      zd.append(layt[e[1]][2])
      
      ud.append(layt[e[1]][0] - layt[e[0]][0])
      vd.append(layt[e[1]][1] - layt[e[0]][1])
      wd.append(layt[e[1]][2] - layt[e[0]][2])

    return {
        'x':xd, 'y':yd, 'z':zd,
        'u':ud, 'v':vd, 'w':wd
    }

  def get_texts(self):
    layt = self.__layt
    xt=[]
    yt=[]
    zt=[]

    for e in self.__graphInfo.get_edges():
      x,y,z = nbym_point(layt[e[0]][0], layt[e[0]][1], layt[e[0]][2], layt[e[1]][0], layt[e[1]][1], layt[e[1]][2], 2, 1)
      xt.append(x)
      yt.append(y)
      zt.append(z)
    
    return{
        'x':xt,
        'y':yt,
        'z':zt,
        'text':self.get_edge_labels()
    }