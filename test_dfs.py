from environment import Environment
from searchAlgorithms.dfs_cam import depthFirstSearch

e = Environment()

s = depthFirstSearch(e,e.cells[2][3])

print(s)