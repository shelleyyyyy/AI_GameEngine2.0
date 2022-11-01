from Infrastructure.node import Node
from constants import constants
from Infrastructure.successorFunction import SuccessorFunction
import time

def iterativeDepthLimitedSearch(environment, root, limit, t):
    
    node = Node(state = root)
    if node.state.cell_type == constants["GOAL_CELL"]:
        return node.actionsList
    
    frontier = [node]
    explored = []
    depth = 0
    while True:
        if len(frontier) == 0:
            return []
        shallow = frontier.pop(len(frontier)-1)
        explored.append(shallow)
        
        sucFunc = SuccessorFunction()
        if depth != limit:
            expand = sucFunc.expand(node = shallow, environment = environment)
            depth+=1
            for n in expand:
                if checklist(n, frontier, explored) != True:
                    if environment.cells[n.state.location.x][n.state.location.y].cell_type == constants["GOAL_CELL"]:
                        print(time.time() - t)
                        return n.actionsList
            
                    frontier.append(n)
        else:
            return iterativeDepthLimitedSearch(environment, root, limit= limit +1, t=t)


def checklist(node, frontier, explored):
    for n in frontier:
        if n.state.location.x == node.state.location.x and n.state.location.y == node.state.location.y and n.state.direction == node.state.direction:
            return True
    for n in explored:
        if n.state.location.x == node.state.location.x and n.state.location.y == node.state.location.y and n.state.direction == node.state.direction:
            return True
    return False

def checkGoalState(node):
    if node.state == constants['GOAL_CELL']:
        return
        
