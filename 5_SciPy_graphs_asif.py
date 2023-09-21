from sympy import var
var( 'return_predecessors  indices limi ')

import numpy as np
from scipy.sparse.csgraph import connected_components , dijkstra , floyd_warshall , bellman_ford , depth_first_order , breadth_first_order
from scipy.sparse import csr_matrix

# SciPy Graphs
# Connected Components

arr = np.array([
  [0, 1, 2],
  [1, 0, 0],
  [2, 0, 0]
])

newarr = csr_matrix(arr)

print(connected_components(newarr))

# Dijkstra
# Find the shortest path from element 1 to 2:

return_predecessors #: boolean (True to return whole path of traversal otherwise False).
indices    # : index of the element to return all paths from that element only.
limi       # : max weight of path.



arr = np.array([
  [0, 1, 2],
  [1, 0, 0],
  [2, 0, 0]
])

newarr = csr_matrix(arr)

print(dijkstra(newarr, return_predecessors=True, indices=0))

# Floyd Warshall
# Find the shortest path between all pairs of elements:

arr = np.array([
  [0, 1, 2],
  [1, 0, 0],
  [2, 0, 0]
])

newarr = csr_matrix(arr)

print(floyd_warshall(newarr, return_predecessors=True))

# Bellman Ford
# Find shortest path from element 1 to 2 with given graph with a negative weight

arr = np.array([
  [0, -1, 2],
  [1, 0, 0],
  [2, 0, 0]
])

newarr = csr_matrix(arr)

print(bellman_ford(newarr, return_predecessors=True, indices=0))

# Depth First Order
# Traverse the graph depth first for given adjacency matrix:

arr = np.array([
  [0, 1, 0, 1],
  [1, 1, 1, 1],
  [2, 1, 1, 0],
  [0, 1, 0, 1]
])

newarr = csr_matrix(arr)

print(depth_first_order(newarr, 1))

# Breadth First Order
# Traverse the graph breadth first for given adjacency matrix

arr = np.array([
  [0, 1, 0, 1],
  [1, 1, 1, 1],
  [2, 1, 1, 0],
  [0, 1, 0, 1]
])

newarr = csr_matrix(arr)

print(breadth_first_order(newarr, 1))










