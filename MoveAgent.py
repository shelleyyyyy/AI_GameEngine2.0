import Action
class MoveAgent:
    percept = None
    cost = []
    action = []

    def __init__(self) -> None:
        pass

    def insertAction(self,action):
        self.action = action

    def obtainPercets():
        pass

    def obtainCosts(self):
        for i in range(len(self.action)):
            self.cost.append(Action.getCosts(self.action[i]))

    def obtainActions():
        pass

    def move():
        """take the action[]
            go through and move the agent in the grid
            need to check if it wont go out of bound
            shouldnt if the search function is working properly"""
        pass

    def printCost(self):
        for i in range(len(self.cost)):
            print(self.cost[i])
        
    
   
        