from gameEngine.environment import Environment
from searchAlgorithms.depthFirstSearch import depthFirstSearch


""" e = Environment()

s = depthFirstSearch(e,e.cells[2][3])

print(s) """

env: Environment = Environment()
env.toString()
solution = depthFirstSearch(environment=env, root=env.root)
print(solution)