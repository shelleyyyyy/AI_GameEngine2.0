from environment import Environment
from searchAlgorithms.dls_cam import depthLimitedSearch
from searchAlgorithms.idls_cam import iterativeDepthLimitedSearch

e = Environment()

#s = depthLimitedSearch(e,e.cells[2][3], 7)
s = depthLimitedSearch(e,e.cells[2][3], 7)
print(s)

