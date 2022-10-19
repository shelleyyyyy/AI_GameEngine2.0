from environment import Environment
from successorFunction import SuccessorFunction
from node import Node

env = Environment()
env.toString()

root_node = Node(env.cells[4][4])

# expand requires a built environment and a root node identified
test = SuccessorFunction().expand(environment=env, node=root_node)

