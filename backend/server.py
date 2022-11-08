from flask import Flask, request, jsonify
from gameEngine.environment import Environment
from searchAlgorithms.breadthFirstSearch import breadthFirstSearch
from searchAlgorithms.depthFirstSearch import depthFirstSearch
from searchAlgorithms.depthLimitedSearch import depthLimitedSearch
from searchAlgorithms.uniformed_cost_search import uniformed_cost_search
from searchAlgorithms.interative_depth_limited_search import iterativeDepthLimitedSearch
from flask_cors import CORS
import time
import threading

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

@app.route("/search", methods=['POST'])
def run_sim():

    print("Trucks", request.json.get("trucks", None))

    trucks = int(request.json.get("trucks", None))
    seed = request.json.get("blocks", None)
    goals = int(request.json.get("goals", None))
    gridSize = int(request.json.get("gridsize", None))
    search_type = request.json.get("search", None)

    env: Environment = Environment(gridSize=gridSize, truckAgentCount=trucks, goalCount=goals, seed=seed)
    grid = env.get_cells_by_type()
    #return search_engine(search_type=search_type, truck=trucks, goals=goals, gridSize=gridSize, seed=seed, grid=grid, env=env)

    threads=[]
    for truck in trucks:
        threads.append(threading.Thread(target=search_engine, args=(search_type, truck, goals, gridSize, seed, grid, env)))
        threads[truck].start()


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
    
    elif search_type == "Depth First Search":
        print(truck, goals, gridSize, "seed:", seed)
        env.toString()
        start = time.time()
        solution = depthFirstSearch(environment=env, root=env.root)
        end = time.time()
        elapsed = end - start
        print(solution)
        return {"solution": solution, "rootX": env.root.location.x, "rootY": env.root.location.y, 
            "direction": (env.root.direction + 2) % 4, "grid": grid, "time": elapsed}

    elif search_type == "Depth Limit Search":
        print(truck, goals, gridSize, "seed:", seed)
        env.toString()
        start = time.time()
        solution = depthLimitedSearch(environment=env, root=env.root, limit=30)
        end = time.time()
        elapsed = end - start
        print(solution)
        return {"solution": solution, "rootX": env.root.location.x, "rootY": env.root.location.y, 
            "direction": (env.root.direction + 2) % 4, "grid": grid, "time": elapsed}

    elif search_type == "Uniform Cost Search":
        print(truck, goals, gridSize, "seed:", seed)
        env.toString()
        start = time.time()
        solution = uniformed_cost_search(environment=env, root=env.root)
        end = time.time()
        elapsed = end - start
        print(solution)
        return {"solution": solution, "rootX": env.root.location.x, "rootY": env.root.location.y, 
            "direction": (env.root.direction + 2) % 4, "grid": grid, "time": elapsed}

    elif search_type == "Iterative Depth Limited Search":
        print(truck, goals, gridSize, "seed:", seed)
        env.toString()
        start = time.time()
        solution = iterativeDepthLimitedSearch(environment=env, root=env.root, limit=0, t=start)
        end = time.time()
        elapsed = end - start
        print(solution)
        return {"solution": solution, "rootX": env.root.location.x, "rootY": env.root.location.y, 
            "direction": (env.root.direction + 2) % 4, "grid": grid, "time": elapsed}

    return 400