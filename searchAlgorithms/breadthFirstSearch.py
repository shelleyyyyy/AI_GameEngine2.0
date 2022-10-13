from constants import constants
from environment import Environment
from node import Node

class BreadthFirstSearch():
    environment: Environment

    def breadthFirstSearch(environment: Environment):
        node: Node = Node()
        if node.state == goal:
            return node
        frontier: list = [node]
        explored: list = []

        while True:
            if len(frontier) == 0: return False
            node: Node = frontier.pop()
            explored.append(node.state)
            

        pass

    def search(rootNode: Node, maxtime):
        pass