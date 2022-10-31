from environment import Environment
from searchAlgorithms.dls_cam import depthLimitedSearch
from searchAlgorithms.idls_cam import iterativeDepthLimitedSearch
import time
e = Environment()

#s = depthLimitedSearch(e,e.cells[2][3], 7)
t = time.time()
s = iterativeDepthLimitedSearch(e,e.cells[2][3], 0, t)
print(s)

