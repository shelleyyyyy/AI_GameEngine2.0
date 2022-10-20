from constants import constants
from environment import Environment
from node import Node
from successorFunction import SuccessorFunction

def breadthFirstSearch(environment: Environment):
    expander = SuccessorFunction()
    root_node: Node = Node(state = environment.cells[2][3])
    if root_node.state.cell_type == constants["GOAL_CELL"]:
        return root_node.actionsList
    frontier: list = [root_node]
    explored: list = []

    while True:
        if len(frontier) == 0: return None
        node: Node = frontier.pop(0)
        explored.append(node.state)
        list = expander.expand(environment=environment, node=node)
        for node in list:
            if check_explored(explored=explored, node=node) and check_frontier(frontier=frontier, node=node):
                print(node.state.location.x, node.state.location.y, node.state.direction)
                if environment.cells[node.state.location.x][node.state.location.y].cell_type == constants["GOAL_CELL"]:
                    return node.actionsList
                else:
                    frontier.append(node)

def check_explored(explored: list, node: Node):
    for x in explored:
        if node.state.location.x == x.location.x and node.state.location.y == x.location.y and node.state.direction == x.direction:
            return False
    return True

def check_frontier(frontier: list, node: Node):
    for x in frontier:
        if node.state.location.x == x.state.location.x and node.state.location.y == x.state.location.y and node.state.direction == x.state.direction:
            return False
    return True

env = Environment()

solution = breadthFirstSearch(environment=env)
print(solution)