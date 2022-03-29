from helper import *

class GraphInfo:
  def __init__(self, adjList, weight, nodeValue):
    self.__adjList = adjList
    self.__weight = weight
    self.__nodeValue = nodeValue
  
  def __str__(self):
    return '\n'.join([f'{key} : {value}' for key, value in self.__dict__.items()])
  
  def get_edges(self):
    try:
      return self.__edges
    except AttributeError:
      edges = []
      for src, tars in enumerate(self.__adjList):
        for tar in tars:
          edges.append((src, tar))
      self.__edges = edges
      return self.__edges

  def get_vertices(self):
    try:
      return self.__vertices
    except AttributeError:
      self.__vertices = max(flatten2d(self.__adjList))+1
      return self.__vertices
  
  def get_node_value(self):
    return self.__nodeValue
  
  def get_weight(self):
    return self.__weight

  def get_adjlist(self):
    return self.__adjList