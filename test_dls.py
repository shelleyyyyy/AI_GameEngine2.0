from environment import Environment
from searchAlgorithms.dls_cam import depthLimitedSearch

e = Environment()

s = depthLimitedSearch(e,e.cells[2][3], 7)

print(s)