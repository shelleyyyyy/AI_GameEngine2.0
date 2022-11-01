from gameEngine.environment import Environment
from searchAlgorithms.interative_depth_limited_search import iterativeDepthLimitedSearch
import time
e = Environment()

#s = depthLimitedSearch(e,e.cells[2][3], 7)
t = time.time()
s = iterativeDepthLimitedSearch(e,e.cells[2][3], 0, t)
print(s)