from constants import constants
from gameEngine.environment import Environment
from Infrastructure.node import Node
from gameEngine.cell import Cell
from Infrastructure.successorFunction import SuccessorFunction

def breadthFirstSearch(environment: Environment, root: Cell):
    expander = SuccessorFunction()
    root_node: Node = Node(state = root)
    if root_node.state.cell_type == constants["GOAL_CELL"]:
        return root_node.actionsList
    frontier: list = [root_node]
    explored = dict()

    while True:
        if len(frontier) == 0: return None
        node: Node = frontier.pop(0)
        explored[node.state.location.x, node.state.location.y, node.state.direction] = node
        list = expander.expand(environment=environment, node=node)
        for node in list:
            if check_explored(explored=explored, node=node) and check_frontier(frontier=frontier, node=node):
                if environment.cells[node.state.location.x][node.state.location.y].cell_type == constants["GOAL_CELL"]:
                    return node.actionsList
                else:
                    frontier.append(node)

def check_explored(explored: list, node: Node):
    key = node.state.location.x, node.state.location.y, node.state.direction
    
    if key in explored.keys():
            return True
    return False

def check_frontier(frontier: list, node: Node):
    for x in frontier:
        if node.state.location.x == x.state.location.x and node.state.location.y == x.state.location.y and node.state.direction == x.state.direction:
            return False
    return True

""" env: Environment = Environment()
env.toString()
solution = breadthFirstSearch(environment=env, root=env.root)
print(solution) """