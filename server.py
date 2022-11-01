from flask import Flask, request, jsonify
from gameEngine.environment import Environment
from searchAlgorithms.breadthFirstSearch import breadthFirstSearch
from searchAlgorithms.depthFirstSearch import depthFirstSearch
from searchAlgorithms.depthLimitedSearch import depthLimitedSearch
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

@app.route("/search", methods=['POST'])
def run_sim():
    search_type = "BFS"

    print("Trucks", request.json.get("trucks", None))

    trucks = request.json.get("trucks", None)
    blocks = request.json.get("blocks", None)
    goals = request.json.get("goals", None)
    gridSize = request.json.get("gridsize", None)

    env: Environment = Environment(gridSize=gridSize, nonPassableCount=blocks, truckAgentCount=trucks, goalCount=goals)
    print(env.cells)
    print(env.get_cells_by_type())

    if search_type == "BFS":
        print(trucks, blocks, goals, gridSize)
        env.toString()
        solution = breadthFirstSearch(environment=env, root=env.root)
        print(solution)
        return {"solution": solution, "rootX": env.root.location.x, "rootY": env.root.location.y, "direction": (env.root.direction + 2) % 4, "grid": jsonify(env.cells)}
    
    elif search_type == "DFS":
        print(trucks, blocks, goals, gridSize)
        env.toString()
        solution = depthFirstSearch(environment=env, root=env.root)
        print(solution)
        return {"solution": solution, "rootX": env.root.location.x, "rootY": env.root.location.y, "direction": (env.root.direction + 2) % 4}

    elif search_type == "DLS":
        print(trucks, blocks, goals, gridSize)
        env.toString()
        solution = depthLimitedSearch(environment=env, root=env.root, limit=7)
        print(solution)
        return {"solution": solution, "rootX": env.root.location.x, "rootY": env.root.location.y, "direction": (env.root.direction + 2) % 4}

    elif search_type == "UCS":
        return {"solution": "solution", "root": "env.root"}

    return 400