from Infrastructure.node import Node
from constants import constants
from Infrastructure.successorFunction import SuccessorFunction
from threading import Lock
import time

def iterativeDepthLimitedSearch(lock: Lock, environment, root, limit, t):

    t = time.time()
    
    node = Node(state = root)
    if node.state.cell_type == constants["GOAL_CELL"]:
        return node.actionsList
    
    frontier = [node]
    explored = dict()
    depth = 0
    while True:
        if len(frontier) == 0:
            return []
        shallow = frontier.pop(len(frontier)-1)
        explored[shallow.state.location.x, shallow.state.location.y, shallow.state.direction] = shallow
        
        sucFunc = SuccessorFunction()
        if depth < limit:
            expand = sucFunc.expand(node = shallow, environment = environment)
            depth = depth + 1
            for n in expand:
                if checklist(n, frontier, explored) != True:
                    current_cell: Cell = environment.cells[n.state.location.x][n.state.location.y]
                    if current_cell.cell_type == constants["GOAL_CELL"] and current_cell.get_found() == False:
                        lock.acquire()
                        current_cell.set_found(True)
                        lock.release()
                        print(time.time() - t)
                        return n.actionsList
            
                    frontier.append(n)
        else:
            return iterativeDepthLimitedSearch(lock=lock, environment=environment, root=root, limit= limit +1, t=t)


def checklist(node, frontier, explored):
    key = node.state.location.x, node.state.location.y, node.state.direction
    for n in frontier:
        if n.state.location.x == node.state.location.x and n.state.location.y == node.state.location.y and n.state.direction == node.state.direction:
            return True
    if key in explored.keys():
            return True
    return False
def checkGoalState(node):
    if node.state == constants['GOAL_CELL']:
        return
        
