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

    print("Trucks", request.json.get("trucks", None))

    trucks = int(request.json.get("trucks", None))
    blocks = int(request.json.get("blocks", None))
    goals = int(request.json.get("goals", None))
    gridSize = int(request.json.get("gridsize", None))
    search_type = request.json.get("search", None)

    env: Environment = Environment(gridSize=gridSize, nonPassableCount=blocks, truckAgentCount=trucks, goalCount=goals)
    grid = env.get_cells_by_type()
    print(grid)

    if search_type == "Breadth First Search":
        print(trucks, blocks, goals, gridSize)
        env.toString()
        solution = breadthFirstSearch(environment=env, root=env.root)
        print(solution)
        return {"solution": solution, "rootX": env.root.location.x, "rootY": env.root.location.y, "direction": (env.root.direction + 2) % 4, "grid": grid}
    
    elif search_type == "Depth First Search":
        print(trucks, blocks, goals, gridSize)
        env.toString()
        solution = depthFirstSearch(environment=env, root=env.root)
        print(solution)
        return {"solution": solution, "rootX": env.root.location.x, "rootY": env.root.location.y, "direction": (env.root.direction + 2) % 4, "grid": grid}

    elif search_type == "Depth Limit Search":
        print(trucks, blocks, goals, gridSize)
        env.toString()
        solution = depthLimitedSearch(environment=env, root=env.root, limit=30)
        print(solution)
        return {"solution": solution, "rootX": env.root.location.x, "rootY": env.root.location.y, "direction": (env.root.direction + 2) % 4, "grid": grid}

    elif search_type == "Uniform Cost Search":
        return {"solution": "solution", "root": "env.root"}

    return 400