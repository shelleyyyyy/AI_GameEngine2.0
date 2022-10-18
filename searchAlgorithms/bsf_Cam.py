from node import Node
from constants import constants
from successorFunction import SuccessorFunction

def breadthFirstSearch(environment):
    node = Node()
    if node.state == constants["GLITTER"]:
        return node
    
    frontier = [node]
    explored = []

    while True:
        if len(frontier) is 0:
            return 'nothing'
        shallow = frontier.pop()
        explored.append(shallow.state)
        
        sucFunc = SuccessorFunction()

        expand = sucFunc.expand(shallow, environment)

        for node in expand:
            frontier.append(node)
        

        

      
