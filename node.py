from copy import deepcopy

class Node:
    def __init__(self, state, parent=None, action=None, actionsList=[], pathCost=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.actionsList = actionsList
        if action is None and parent is None:
            self.pathCost = pathCost
        else:
            self.pathCost = self.parent.pathCost + self.action.getStepCost(action) # waiting on action class

        if len(parent.actionList) == 0:
            self.actionsList.add(0, self.action)
        else:
            self.actionsList = parent.actionsList
            self.actionsList.add(self.action);
        

    def copyOfNode(self):
        return deepcopy(self)

    def equals(self, obj):

        if obj is None: return False

        if self == obj: return True

        if not isinstance(obj, Node): return False

        inner = Node(obj)

        if self.state is None:
            print("Self")
        if inner.state is None:
            print("inner")

        if (self.state.equals(inner.state) and self.pathCost == inner.pathCost 
                and self.hValue == inner.hValue and self.action.equals(inner.action)):
            return True

        return False
    

class NodeComparator:
    def __init__(self, goals, searchType):
        self.goals = goals
        self.searchType = searchType

    def compareType(self, searchType):
        match searchType:
            case "UniformedCostSearch":
                # waiting for heuristics
            case "GreedyBestFirstSearch":
                # waiting for heuristics
            case "AStarSearch":
                # waiting for heuristics
