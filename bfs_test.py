from constants import constants
from environment import Environment
from successorFunction import SuccessorFunction
from node import Node

#######################################################
# William Shelley BFS Implemintation
# Help Recieved: Discussed with cole corson, googled basic python syntax, class notes and materials
#######################################################

# helper function to check if noe is already explored or already in frontier queue
def isNodeInList(nodes, node):
    for n in nodes:
        if n.state.location.x == node.state.location.x and n.state.location.y == node.state.location.y and n.state.direction == node.state.direction:
            return True
    return False

# helper function to check for goal state
def isGoal(env, node):
    if env.cells[node.state.location.x][node.state.location.y].cell_type == constants["GOAL_CELL"]:
        return True

    return False

def breadFirstSearch(root_node, env):
    # frontier queue
    queue = [root_node]
    # explored list
    explored = []

    # checks if root node is goal
    if isGoal(env, root_node):
        return root_node.state.location

    while True:
        # if frontier is empty return false because the search has failed
        if len(queue) < 1:
            return False
        
        # pop the node at the beggining of the queue
        current_node = queue.pop(0)
        # add the node to the explored list 
        explored.append(current_node)
        # iterate through the expanded nodes
        for n in s.expand(environment=env, node=current_node):
            # check if the node is already in explored or already in frontier queue
            if isNodeInList(explored, n) or isNodeInList(queue, n):
                continue
            # checks for goal
            if isGoal(env, n):
                return n.state.location.toString()
            # appends expanded node to the end of the frontier queue
            queue.append(n)


# initialize environment
env = Environment()

# set root node, truck agent starting point
root_node = Node(state = env.cells[0][3])

# bring in succesor function
s = SuccessorFunction()

print("TRUCK STARTING LOCATION")
print("*"*30)
print(root_node.state.toString())
print("*"*30)
print("*"*30)
print("FOUND GOAL")
print(breadFirstSearch(root_node, env))
print("*"*30)