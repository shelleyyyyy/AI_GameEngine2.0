from gameEngine.environment import Environment
import threading
import time
from searchAlgorithms.breadthFirstSearch import breadthFirstSearch

def search_engine(search_type, truck, goals, gridSize, seed, grid, env, results):
    if search_type == "Breadth First Search":
        env.toString()
        start = time.time()
        solution = breadthFirstSearch(environment=env, root=env.root[0])
        end = time.time()
        elapsed = end - start
        print(solution)
        results.apend({"solution": solution, "rootX": env.root[0].location.x, "rootY": env.root[0].location.y, 
            "direction": (env.root[0].direction + 2) % 4, "grid": grid, "time": elapsed})

actions = []
trucks = 3
seed = "adsf"
goals = 3
gridSize = 10
search_type = "Breadth First Search"

env: Environment = Environment(gridSize=gridSize, truckAgentCount=trucks, goalCount=goals, seed=seed)
grid = env.get_cells_by_type()
#return search_engine(search_type=search_type, truck=trucks, goals=goals, gridSize=gridSize, seed=seed, grid=grid, env=env)

truck_threads=[]
for truck in trucks:
    truck_threads.append(threading.Thread(target=search_engine, args=(search_type, truck, goals, gridSize, seed, grid, env, actions)))
    truck_threads[truck].start()

print(actions)



