import random
  
def distribute(node, edge):
  n = random.randint(1, node)
  ret = [0]*n
  for _ in range(edge):
    ret[random.randint(0, n-1)] += 1
  return ret

def random_adjList(dist, node):
  ret = []
  node_numbers = [i for i in range(node)]
  for i in dist:
    ret.append(random.sample(node_numbers, i))
  return ret

def random_weight(dist, min=-100, max=100):
  ret = []
  for i in dist:
    ret.append([random.randint(min, max) 
                for _ in range(i)])
  return ret

def random_nodeValue(node, min=0, max=100):
  return [random.randint(min, max)
    for _ in range(node)]

def random_graph(node=100, edge=300):

  dist = distribute(node,edge)
  adjList = random_adjList(dist, node)
  weight = random_weight(dist)
  nodeValue = random_nodeValue(node)

  graphInfo = {
      'adjList' : adjList,
      'weight' : weight,
      'nodeValue' : nodeValue,
  }
  print(graphInfo)
  return graphInfo


