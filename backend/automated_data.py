import random
import json
from gameEngine.environment import Environment
import threading
import time
from searchAlgorithms.breadthFirstSearch import breadthFirstSearch
from searchAlgorithms.depthFirstSearch import depthFirstSearch
from searchAlgorithms.depthLimitedSearch import depthLimitedSearch
from searchAlgorithms.interative_depth_limited_search import iterativeDepthLimitedSearch
from searchAlgorithms.uniformed_cost_search import uniformed_cost_search
import pandas as pd

def input(): 
    bfs_data = []
    dfs_data = []
    dls_data = []
    ucs_data = []
    idls_data = []

    for index in range(0, 20):
        trucks = 1
        seed = random.randint(0, 1000)
        gridSize = 5

        bfs_result = automated_experiments(trucks=trucks, seed=seed, gridSize=gridSize, search_type="Breadth First Search")
        dfs_result = automated_experiments(trucks=trucks, seed=seed, gridSize=gridSize, search_type="Depth First Search")
        dls_result = automated_experiments(trucks=trucks, seed=seed, gridSize=gridSize, search_type="Depth Limit Search")
        ucs_result = automated_experiments(trucks=trucks, seed=seed, gridSize=gridSize, search_type="Uniform Cost Search")
        #idls_result = automated_experiments(trucks=trucks, seed=seed, gridSize=gridSize, search_type="Iterative Depth Limited Search")
        
        bfs_data.append(bfs_result)
        dfs_data.append(dfs_result)
        dls_data.append(dls_result)
        ucs_data.append(ucs_result)
        #idls_data.append(idls_result)
    
    with open('bfsdata.json', 'w') as f:
        json.dump(bfs_data, f)

    with open('dfsdata.json', 'w') as f:
        json.dump(dfs_data, f)

    with open('dlsdata.json', 'w') as f:
        json.dump(dls_data, f)

    with open('ucsdata.json', 'w') as f:
        json.dump(ucs_data, f)

    #with open('idlsdata.json', 'w') as f:
        #json.dump(idls_data, f)

def test():
    trucks = 1
    seed = 225
    gridSize = 5
    search_type = "Breadth First Search"
    result = automated_experiments(trucks=trucks, seed=seed, gridSize=gridSize, search_type=search_type)
    print("results", result)

def automated_experiments(trucks, seed, gridSize, search_type):
    
    goals = trucks

    print("trucks", trucks, "seed", seed, "goals", goals, "gridSize", gridSize, "searchType", search_type)

    env: Environment = Environment(gridSize=gridSize, truckAgentCount=trucks, goalCount=goals, seed=seed)
    grid = env.get_cells_by_type()
    #return search_engine(search_type=search_type, truck=trucks, goals=goals, gridSize=gridSize, seed=seed, grid=grid, env=env)
    

    results = []
    lock = threading.Lock()
    threads=[]
    for num in range(0, trucks):
        root: Cell = env.root[num]
        t = threading.Thread(target=search_engine, args=(search_type, trucks, goals, gridSize, seed, grid, env, root, results, lock))
        t.start()
        threads.append(t)
    for thread in threads:
        thread.join()

    longest_path, shortest_path, longest_time, shortest_time = post_process(results)

    return { 
        "grid": grid, 
        "stats": {"size": gridSize, "longestPath": longest_path, "shortestPath": shortest_path, "longestTime": longest_time, 
            "shortestTime": shortest_time, "numTrucks": trucks, "searchType": search_type}, 
        "agents": results
        }


def search_engine(search_type, truck, goals, gridSize, seed, grid, env, root, results, lock):
    if search_type == "Breadth First Search":
        start = time.time()
        solution = breadthFirstSearch(environment=env, root=root, lock=lock)
        end = time.time()
        elapsed = end - start
        path = len(solution) if solution != None else None
        results.append({
            "position": {"x": root.location.x, "y": root.location.y}, 
            "status": get_status(root.direction),
            "sequence": solution,  
            "stats": {
                "id": 1,
                "time": elapsed,
                "path": solution,
            } 
        })

    elif search_type == "Depth First Search":
        print(truck, goals, gridSize, "seed:", seed)
        
        start = time.time()
        solution = depthFirstSearch(environment=env, root=root, lock=lock)
        end = time.time()
        elapsed = end - start
        path = len(solution) if solution != None else None
        results.append({
            "position": {"x": root.location.x, "y": root.location.y}, 
            "status": get_status(root.direction),
            "sequence": solution,  
            "stats": {
                "id": 1,
                "time": elapsed,
                "path": solution,
            } 
        })

    elif search_type == "Depth Limit Search":
        print(truck, goals, gridSize, "seed:", seed)
        
        start = time.time()
        solution = depthLimitedSearch(environment=env, root=root, lock=lock, limit=300)
        end = time.time()
        elapsed = end - start
        path = len(solution) if solution != None else None
        results.append({
            "position": {"x": root.location.x, "y": root.location.y}, 
            "status": get_status(root.direction),
            "sequence": solution,  
            "stats": {
                "id": 1,
                "time": elapsed,
                "path": solution,
            } 
        })

    elif search_type == "Uniform Cost Search":
        print(truck, goals, gridSize, "seed:", seed)
        
        start = time.time()
        solution = uniformed_cost_search(environment=env, root=root, lock=lock)
        end = time.time()
        elapsed = end - start
        path = len(solution) if solution != None else None
        results.append({
            "position": {"x": root.location.x, "y": root.location.y}, 
            "status": get_status(root.direction),
            "sequence": solution,  
            "stats": {
                "id": 1,
                "time": elapsed,
                "path": solution,
            } 
        })

    elif search_type == "Iterative Depth Limited Search":
        print(truck, goals, gridSize, "seed:", seed)
        
        start = time.time()
        solution = iterativeDepthLimitedSearch(environment=env, root=root, lock=lock, limit=1, t=start)
        end = time.time()
        elapsed = end - start
        path = len(solution) if solution != None else None
        results.append({
            "position": {"x": root.location.x, "y": root.location.y}, 
            "status": get_status(root.direction),
            "sequence": solution,  
            "stats": {
                "id": 1,
                "time": elapsed,
                "path": solution,
            } 
        })

    return 400

def post_process(results):
    longest_path = 0
    shortest_path = 500
    longest_time = 0
    shortest_time = 5000

    if results == []:
        return 0, 0, 0, 0

    for solution in results:
        if solution['sequence'] != None:
            print(solution)
            if len(solution['sequence']) > longest_path:
                longest_path = len(solution['sequence'])
            if len(solution['sequence']) < shortest_path:
                shortest_path = len(solution['sequence'])
        if solution['stats']['time'] > longest_time:
            longest_time = solution['stats']['time']
        if solution['stats']['time'] < shortest_time:
            shortest_time = solution['stats']['time']
    return longest_path, shortest_path, longest_time, shortest_time

def get_status(direction):
    direction = (direction + 2) % 4 
    if direction == 0:
        return 'a-u'
    elif direction == 1:
        return 'a-r'
    elif direction == 2:
        return 'a-d'
    else:
        return 'a-l'


input()