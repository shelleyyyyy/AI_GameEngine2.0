from Infrastructure.node import Node
from constants import constants
from Infrastructure.successorFunction import SuccessorFunction
from gameEngine.environment import Environment
from gameEngine.cell import Cell
import time

def depthFirstSearch(environment: Environment, root: Cell):
    t = time.time()
    node = Node(state = root)
    if node.state.cell_type == constants["GOAL_CELL"]:
        return node.actionsList
    fIndex = 0
    eIndex = 0
    frontier = [node]
    explored = dict()
    
    while True:
        if len(frontier) == 0:
            return []
        shallow = frontier.pop(len(frontier)-1)
        #explored.append(shallow)
        #explored[shallow] = {shallow.state.location.x, shallow.state.location.y, shallow.state.direction}
        explored[{shallow.state.location.x, shallow.state.location.y, shallow.state.direction}] = shallow
        sucFunc = SuccessorFunction()
        expand = sucFunc.expand(node = shallow, environment = environment)
        
        for n in expand:
            if checklist(n, frontier, explored) != True:
                if environment.cells[n.state.location.x][n.state.location.y].cell_type == constants["GOAL_CELL"]:
                    print(time.time() - t)
                    return n.actionsList
            
                frontier.append(n)


def checklist(node, frontier, explored):
    key = {node.state.location.x, node.state.location.y, node.state.direction}
    for n in frontier:
        if n.state.location.x == node.state.location.x and n.state.location.y == node.state.location.y and n.state.direction == node.state.direction:
            return True
    if key in explored.keys():
            return True
    return False

def checkGoalState(node):
    if node.state == constants['GOAL_CELL']:
        return
        
