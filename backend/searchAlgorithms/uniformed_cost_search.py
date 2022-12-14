from Infrastructure.node import Node
from constants import constants
from Infrastructure.successorFunction import SuccessorFunction
from threading import Lock
import time

#quicksort methods
def partition(list, low, high):
 
    pivot = list[high]
 
    i = low - 1
 
    for j in range(low, high):
        if list[j].pathCost <= pivot.pathCost:
 
            i = i + 1

            (list[i], list[j]) = (list[j], list[i])
 
    (list[i + 1], list[high]) = (list[high], list[i + 1])
 
    return i + 1
 
 
def quickSort(list, low, high):
    if list[low].pathCost < list[high].pathCost:
 
        pi = partition(list, low, high)
 
        quickSort(list, low, pi - 1)
 
        quickSort(list, pi + 1, high)



def uniformed_cost_search(environment, root, lock):

    t = time.time()

    node = Node(state = root)
    if node.state.cell_type == constants["GOAL_CELL"]:
        return node.actionsList
    
    frontier = [node]
    explored = dict()

    while True:
        if len(frontier) == 0:
            return []
        shallow = frontier.pop(0)
        explored[shallow.state.location.x, shallow.state.location.y, shallow.state.direction] = shallow
        
        sucFunc = SuccessorFunction()

        expand = sucFunc.expand(node = shallow, environment = environment)
        
        for n in expand:
            if checklist(n, frontier, explored) != True:
            
                frontier.append(n)
                try:
                    quickSort(frontier, 0, len(frontier) - 1)
                except:
                    pass

                current_cell: Cell = environment.cells[n.state.location.x][n.state.location.y]
                if current_cell.cell_type == constants["GOAL_CELL"] and current_cell.get_found() == False:
                    lock.acquire()
                    current_cell.set_found(True)
                    lock.release()
                    print(time.time() - t)
                    return n.actionsList


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
        

      
