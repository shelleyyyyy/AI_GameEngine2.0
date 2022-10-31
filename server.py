from flask import Flask, request, jsonify
from environment import Environment
from breadthFirstSearch import breadthFirstSearch

app = Flask(__name__)

@app.route("/search", methods=['POST'])
def run_sim():
    search_type = "BFS"

    if search_type == "BFS":
        trucks = request.json.get("trucks", None)
        blocks = request.json.get("blocks", None)
        goals = request.json.get("goals", None)
        gridSize = request.json.get("gridSize", None)
        print(trucks, blocks, goals, gridSize)
        env: Environment = Environment(gridSize=gridSize, nonPassableCount=blocks, truckAgentCount=trucks, goalCount=goals)
        env.toString()
        solution = breadthFirstSearch(environment=env, root=env.root)
        print(solution)
        return {"solution": solution, "root": env.root}
    
    elif search_type == "DFS":
        return {"solution": "solution", "root": "env.root"}
    elif search_type == "DLS":
        return {"solution": "solution", "root": "env.root"}
    elif search_type == "UCS":
        return {"solution": "solution", "root": "env.root"}

    return 400