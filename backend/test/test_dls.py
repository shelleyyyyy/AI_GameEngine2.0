from gameEngine.environment import Environment
from searchAlgorithms.depthLimitedSearch import depthLimitedSearch

""" e = Environment()

s = depthLimitedSearch(e,e.cells[2][3], 7)

print(s) """

env: Environment = Environment()
env.toString()
solution = depthLimitedSearch(environment=env, root=env.root, limit=7)
print(solution)