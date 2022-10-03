import Action
# from concurrent.futures import ThreadPoolExecutor
import threading
from cell import Cell
from truckAgent import TruckAgent
from environment import Environment
from open import Open
class MoveAgent:
    
    def __init__(self, agent):
        self.agent = agent
        self.percept = None
        self.cost = []
        self.action = []
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

    def move(self):
        truck = self.agent
        x = None
        y = None
        for i in range(len(self.action)):
            if self.action[i] == 'north':
                
                x = self.agent.location.x
                y = self.agent.location.y
                Environment.cells[x][y].setType(Open())
                Environment.cells[x][y+1].setType(truck)
                self.agent.updateLocation(Environment.cells[x][y+1])
            elif self.action[i] == 'east':
                x = self.agent.location.x
                y = self.agent.location.y
                Environment.cells[x][y].setType(Open())
                Environment.cells[x+1][y].setType(truck)
                self.agent.updateLocation(Environment.cells[x+1][y])
            elif self.action[i] == 'west':
                x = self.agent.location.x
                y = self.agent.location.y
                Environment.cells[x][y].setType(Open())
                Environment.cells[x-1][y].setType(truck)
                self.agent.updateLocation(Environment.cells[x-1][y])
            else:
                x = self.agent.location.x
                y = self.agent.location.y
                Environment.cells[x][y].setType(Open())
                Environment.cells[x][y-1].setType(truck)
                self.agent.updateLocation(Environment.cells[x][y-1])

    def start(self):
        t = threading.Thread(target=self.move)
        t.start()
        self.obtainCosts()
        self.move()
        t.join()

    def printCost(self):
        for i in range(len(self.cost)):
            print(self.cost[i])
        
    
   
        