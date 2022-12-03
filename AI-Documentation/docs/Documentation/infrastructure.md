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

<Mermaid chart = 'classDiagram
class SuccessorFunction{
goForward(Environment, Cell): Node
expand(Node, Environment): list
}'/>