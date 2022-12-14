from constants import constants
from gameEngine.environment import Environment
from Infrastructure.node import Node
from gameEngine.cell import Cell
from threading import  Lock
from Infrastructure.heuristic import hueristics
from Infrastructure.successorFunction import SuccessorFunction

def aStar(node: Cell, environment: Environment):

    expander = SuccessorFunction()
    openList = []
    closedList = {}
    currentNode: Node = Node(state = node)
    
    nodeHuristic = hueristics(node, environment)

    currentNode.setHueritic(nodeHuristic)

    openList.append(currentNode)

    while(len(openList)!=0):

        bestNode: Node = lowestHueristic(openList)

        currentCell : Cell = environment.cells[bestNode.state.location.x][bestNode.state.location.y]
        if currentCell.cell_type == constants["GOAL_CELL"] and currentCell.get_found() == False:
            return bestNode.actionsList

        key = (bestNode.state.location.x, bestNode.state.location.y, bestNode.state.direction, bestNode.hueritic)
        closedList[key] = openList.remove(bestNode)

        list = expander.expand(environment=environment, node=node)

        for node in list:

            pass

        #successorfunction

def check_explored(explored: dict, node: Node):
    key = (node.state.location.x, node.state.location.y, node.state.direction)
    
    if key in explored.keys():
        return False
    return True
    
def lowestHueristic(openList):
    if len(openList) ==1:
        return openList[0]
    else:
        pass