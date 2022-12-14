from constants import constants
from gameEngine.environment import Environment
from Infrastructure.node import Node
from gameEngine.cell import Cell
from threading import  Lock
from Infrastructure.heuristic import hueristics

def aStar(node: Cell, environment: Environment):
    openList = []
    closedList = []
    currentNode: Node = Node(state = node)
    
    nodeHuristic = hueristics(node, environment)

    currentNode.setHueritic(nodeHuristic)

    openList.append(currentNode)

    while(len(openList)!=0):

        bestNode: Node = lowestHueristic(openList)

        currentCell : Cell = environment.cells[bestNode.state.location.x][bestNode.state.location.y]
        if currentCell.cell_type == constants["GOAL_CELL"] and currentCell.get_found() == False:
            return bestNode.actionsList

        closedList.append(openList.remove(bestNode))

        #successorfunction

def lowestHueristic(openList):
    if len(openList) ==1:
        return openList[0]
    else:
        pass