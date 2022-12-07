from gameEngine.environment import Environment
from searchAlgorithms.breadthFirstSearch import breadthFirstSearch
from gameEngine.cell import Cell
import time
import threading

gridSize = 5
trucks = 1
goals = 1
seed = 'abc'

env: Environment = Environment(gridSize=gridSize, truckAgentCount=trucks, goalCount=goals, seed=seed)
grid = env.get_cells_by_type()

results = []
lock = threading.Lock()
root: Cell = env.root[0]

solution = breadthFirstSearch(environment=env, root=root, lock=lock)

print(solution)