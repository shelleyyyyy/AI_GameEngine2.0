class Node:
    def __init__(self, state, parent=None, action=None):
        self.state = state
        self.parent = parent
        self.action = action
        self.actionsList = []
        self.pathCost = 0 if action is None and parent is None else self.parent.getPathCost() + self.action.getPathCost(action)

    class NodeComparator:
        def __init__(self, goals, searchType):
            self.goals = goals
            self.searchType = searchType

        def compareType(self, searchType):
            # match searchType:
            #     case "UniformedCostSearch":
            #         #do 
            #     case "GreedyBestFirstSearch":

            #     case "AStarSearch":
            pass