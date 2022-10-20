from constants import constants
from environment import Environment
from successorFunction import SuccessorFunction
from node import Node

env = Environment()
env.toString()

root_node = Node(state = env.cells[2][3])

# expand requires a built environment and a root node identified
test = SuccessorFunction()
list = test.expand(environment=env, node=root_node)
for node in list:
    print(node.action)
    print(node.actionsList)
    print()
node = list[0]
if env.cells[node.state.location.x][node.state.location.y].cell_type == constants["GOAL_CELL"]:
    print("GOAL FOUND")
else:
    list1 = test.expand(environment=env, node=list[0])
list2 = test.expand(environment=env, node=list[1])
list3 = test.expand(environment=env, node=list[2])

for node in list1:
    print("List 1")
    print(node.action)
    print(node.actionsList)
    print()
for node in list2:
    print("List 2")
    print(node.action)
    print(node.actionsList)
    print()
for node in list3:
    print("List 3")
    print(node.action)
    print(node.actionsList)
    print()

