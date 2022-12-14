---
sidebar_label: 'Search-Algorithms'
sidebar_position: 3
---
import { Mermaid } from 'mdx-mermaid/Mermaid';

<Mermaid chart = 'classDiagram
class BFS{
breadFirstSearch(Environment, Cell, Lock): list
check_explored(list, Node): bool
check_frontier(list, Node): bool
}'/>

BreadthFirstSearch has a rootNode which is the starting point of the search algorithm. 
The check explored and check frontier are to check the lists to make sure no duplicated node is added. 
Will search until a goal if found or its not able to search any new nodes. 


<Mermaid chart = 'classDiagram
class DFS{
depthFirstSearch(Environment, Cell, Lock): list
checklist(Node, list, list): bool
}'/>

DepthFirstSearch has a rootNode which is the starting point of the search algorithm.
The check explored and check frontier are to check the lists to make sure no duplicated node is added. 
Will search until a goal if found or its not able to search any new nodes. 

<Mermaid chart = 'classDiagram
class DLS{
depthLimitedSearch(Environment, Cell, limit): list
checklist(Node, list, list): bool
}'/>

DepthLimitedSearch has a rootNode which is the starting point of the search algorithm.
The check explored and check frontier are to check the lists to make sure no duplicated node is added. 
Will search until a goal if found or its not able to search any new nodes or the search hits the limit. 


<Mermaid chart = 'classDiagram
class IDLS{
depthLimitedSearch(Environment, Cell, limit, time): list
checklist(Node, list, list): bool
}'/>

IterativeDeepeningDepthFirstSearch has a rootNode which is the starting point of the search algorithm.
The check explored and check frontier are to check the lists to make sure no duplicated node is added. 
Will search until a goal if found or its not able to search any new nodes  or a limit is hit.
If the limit is hit, then the limit will be increase. 

<Mermaid chart = 'classDiagram
class UCS{
partition(list, low, high): int
quickSort(list, low, high)
uniformed_cost_search(environment, root): list
checklist(Node, list, list): bool
}'/>

UCS has a rootNode which is the starting point of the search algorithm.
The check explored and check frontier are to check the lists to make sure no duplicated node is added. 
Will search until a goal if found or its not able to search any new nodes. 