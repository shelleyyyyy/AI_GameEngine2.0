---
sidebar_label: 'Search-Algorithms'
sidebar_position: 3
---

<Mermaid chart = 'classDiagram
class BFS{
breadFirstSearch(Environment, Cell, Lock): list
check_explored(list, Node): bool
check_frontier(list, Node): bool
}'/>

<Mermaid chart = 'classDiagram
class DFS{
depthFirstSearch(Environment, Cell, Lock): list
checklist(Node, list, list): bool
}'/>

<Mermaid chart = 'classDiagram
class DLS{
depthLimitedSearch(Environment, Cell, limit): list
checklist(Node, list, list): bool
}'/>

<Mermaid chart = 'classDiagram
class DLS{
depthLimitedSearch(Environment, Cell, limit): list
checklist(Node, list, list): bool
}'/>

<Mermaid chart = 'classDiagram
class IDLS{
depthLimitedSearch(Environment, Cell, limit, time): list
checklist(Node, list, list): bool
}'/>

<Mermaid chart = 'classDiagram
class UCS{
partition(list, low, high): int
quickSort(list, low, high)
uniformed_cost_search(environment, root): list
checklist(Node, list, list): bool
}'/>