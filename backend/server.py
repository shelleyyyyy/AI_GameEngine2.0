from flask import Flask, request, jsonify
from gameEngine.environment import Environment
from searchAlgorithms.breadthFirstSearch import breadthFirstSearch
from searchAlgorithms.depthFirstSearch import depthFirstSearch
from searchAlgorithms.depthLimitedSearch import depthLimitedSearch
from searchAlgorithms.uniformed_cost_search import uniformed_cost_search
from searchAlgorithms.interative_depth_limited_search import iterativeDepthLimitedSearch
from flask_cors import CORS
from gameEngine.cell import Cell
import time
import threading

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

@app.route("/search", methods=['POST'])
def run_sim():

    print("Trucks", request.json.get("trucks", None))

    trucks = int(request.json.get("trucks", None))
    seed = request.json.get("seed", None)
    goals = int(request.json.get("trucks", None))
    gridSize = int(request.json.get("gridsize", None))
    search_type = request.json.get("search", None)

    print("trucks", trucks, "seed", seed, "goals", goals, "gridSize", gridSize, "searchType", search_type)

    env: Environment = Environment(gridSize=gridSize, truckAgentCount=trucks, goalCount=goals, seed=seed)
    grid = env.get_cells_by_type()
    #return search_engine(search_type=search_type, truck=trucks, goals=goals, gridSize=gridSize, seed=seed, grid=grid, env=env)
    env.toString()

    results = []
    lock = threading.Lock()
    threads=[]
    for num in range(0, trucks):
        root: Cell = env.root[num]
        print(root.location.x, root.location.y)
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
        print(solution)
        results.append({
            "position": {"x": root.location.x, "y": root.location.y}, 
            "status": get_status(root.direction),
            "sequence": solution,  
            "stats": {
                "id": 1,
                "time": elapsed,
                "path": len(solution),
            } 
        })
    
    elif search_type == "Depth First Search":
        print(truck, goals, gridSize, "seed:", seed)
        env.toString()
        start = time.time()
        solution = depthFirstSearch(environment=env, root=root, lock=lock)
        end = time.time()
        elapsed = end - start
        print(solution)
        results.append({
            "position": {"x": root.location.x, "y": root.location.y}, 
            "status": get_status(root.direction),
            "sequence": solution,  
            "stats": {
                "id": 1,
                "time": elapsed,
                "path": len(solution),
            } 
        })

    elif search_type == "Depth Limit Search":
        print(truck, goals, gridSize, "seed:", seed)
        env.toString()
        start = time.time()
        solution = depthLimitedSearch(environment=env, root=root, lock=lock, limit=300)
        end = time.time()
        elapsed = end - start
        print(solution)
        results.append({
            "position": {"x": root.location.x, "y": root.location.y}, 
            "status": get_status(root.direction),
            "sequence": solution,  
            "stats": {
                "id": 1,
                "time": elapsed,
                "path": len(solution),
            } 
        })

    elif search_type == "Uniform Cost Search":
        print(truck, goals, gridSize, "seed:", seed)
        env.toString()
        start = time.time()
        solution = uniformed_cost_search(environment=env, root=root, lock=lock)
        end = time.time()
        elapsed = end - start
        print(solution)
        results.append({
            "position": {"x": root.location.x, "y": root.location.y}, 
            "status": get_status(root.direction),
            "sequence": solution,  
            "stats": {
                "id": 1,
                "time": elapsed,
                "path": len(solution),
            } 
        })

    elif search_type == "Iterative Depth Limited Search":
        print(truck, goals, gridSize, "seed:", seed)
        env.toString()
        start = time.time()
        solution = iterativeDepthLimitedSearch(environment=env, root=root, lock=lock, limit=0, t=start)
        end = time.time()
        elapsed = end - start
        print(solution)
        results.append({
            "position": {"x": root.location.x, "y": root.location.y}, 
            "status": get_status(root.direction),
            "sequence": solution,  
            "stats": {
                "id": 1,
                "time": elapsed,
                "path": len(solution),
            } 
        })

    return 400

def post_process(results):
    longest_path = 0
    shortest_path = 500
    longest_time = 0
    shortest_time = 5000

    for solution in results:
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

