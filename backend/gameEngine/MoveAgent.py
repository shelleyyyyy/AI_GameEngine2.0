import gameEngine.Action as Action
# from concurrent.futures import ThreadPoolExecutor
import threading
from gameEngine.cell import Cell
from gameEngine.location import Location
from gameEngine.truckAgent import TruckAgent
from gameEngine.environment import Environment
from constants import constants
class MoveAgent:
    
    def __init__(self, agent: TruckAgent, enviroment: Environment):
        self.agent = agent
        self.percept = None
        self.cost = []
        self.action = []
        self.enviroment = enviroment
        pass

    def insertAction(self,action):
        self.action = action
        self.obtainCosts()
        self.move()

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
                self.enviroment.cells[x][y].setType(constants['BLANK'])
                self.enviroment.cells[x][y-1].setType(truck)
                #self.agent.updateLocation(self.enviroment.cells[x][y-1])
                self.agent.updateLocation(Location(x,y-1))

            elif self.action[i] == 'east':
                x = self.agent.location.x
                y = self.agent.location.y
                Environment.cells[x][y].setType(constants['BLANK'])
                Environment.cells[x+1][y].setType(truck)
                self.agent.updateLocation(Location(x+1,y))

            elif self.action[i] == 'west':
                x = self.agent.location.x
                y = self.agent.location.y
                Environment.cells[x][y].setType(constants['BLANK'])
                Environment.cells[x-1][y].setType(truck)
                self.agent.updateLocation(Location(x-1,y))

            elif self.action[i] == 'south':
                x = self.agent.location.x
                y = self.agent.location.y
                Environment.cells[x][y].setType(constants['BLANK'])
                Environment.cells[x][y+1].setType(truck)
                self.agent.updateLocation(Location(x,y+1))
            elif self.action[i] == 'northF':
                self.agent.direction = constants['FACING_NORTH']
            elif self.action[i] == 'southF':
                self.agent.direction = constants['FACING_SOUTH']
            elif self.action[i] == 'eastF':
                self.agent.direction = constants['FACING_EAST']
            elif self.action[i] == 'westF':
                self.agent.direction = constants['FACING_WEST']



    def start(self, action):
        t = threading.Thread(target=self.move)
        t.start()
        self.insertAction(action)
        t.join()

    def printCost(self):
        for i in range(len(self.cost)):
            print(self.cost[i])
        
    
   
        