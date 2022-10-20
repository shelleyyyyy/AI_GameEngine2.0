from node import Node
from constants import constants
from successorFunction import SuccessorFunction

def breadthFirstSearch(environment, agent):
    node = Node(state = agent.state)
    if node.state == constants["GLITTER"]:
        return node.actionsList
    
    frontier = [node]
    explored = []

    while True:
        if len(frontier) is 0:
            return []
        shallow = frontier.pop()
        explored.append(shallow)
        
        sucFunc = SuccessorFunction()

        expand = sucFunc.expand(shallow, environment)

        for node in expand:
            if node.state == constants['GOAL_CELL']:
                return node.actionsList
            if checklist(node, frontier, explored) != True:
                frontier.append(node)


def checklist(node, frontier, explored):
    for n in frontier:
        if n.state.location.x and n.state.location.y == node.state.location.x and node.state.location.y:
            return True
    for n in explored:
        if n.state.location.x and n.state.location.y == node.state.location.x and node.state.location.y:
            return True
    return False

def checkGoalState(node):
    if node.state == constants['GOAL_CELL']:
        return
        

      
