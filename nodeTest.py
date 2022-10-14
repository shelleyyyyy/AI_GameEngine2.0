from node import Node

node1 = Node()
node2 = node1
node3 = node1.copyOfNode()

print(node1.equals(node2))
print(node1.equals(node3))