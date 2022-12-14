---
sidebar_label: 'Ingrastructure'
sidebar_position: 2
---

import { Mermaid } from 'mdx-mermaid/Mermaid';

<Mermaid chart = 'classDiagram
class Node{
state
parent
action
actionList: []
pathCost
ID: uuid
copyOfNode(): deepcopy()
equals(object): bool
}'/>

The Node class holds the state of the node, the parent node, action of the node, the list of actions from its ancestors, its own id. 
Node is what is benig used for our Successor function to create the paths and action lists that our agents follow. 

<Mermaid chart = 'classDiagram
class SuccessorFunction{
goForward(Environment, Cell): Node
expand(Node, Environment): list
}'/>

Successor Funciton is getting the next state by expanding on possible actions. 