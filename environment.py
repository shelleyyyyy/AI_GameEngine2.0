from cell import Cell
from blocked import Blocked
from goal import Goal
from truckAgent import TruckAgent

class Environment:
    def __init__(self, gridSize=5, nonPassableCount=5, truckAgentCount=1, goalCount=1):
        self.gridSize = gridSize
        self.cells = []
        self.trucks = []
        self.goals = []
        self.percepts = []
        self.nonPassableCount = nonPassableCount
        self.truckAgentCount = truckAgentCount
        self.goalCount = goalCount

        self.makeCells()
        self.populateEnv()

    def makeCells(self):
        for x in range(self.gridSize):
            cellRow = []
            for y in range(self.gridSize):
                cellRow.append(Cell(x, y))
            self.cells.append(cellRow)
    
    def populateEnv(self):
        self.cells[0][2].setType(Blocked())
        self.cells[1][3].setType(Blocked())
        self.cells[2][2].setType(Blocked())

        self.cells[2][1].setType(Goal())
        self.cells[4][3].setType(Blocked())
        self.cells[4][4].setType(TruckAgent(4,4))
        self.trucks.append(self.cells[4][4].type)

    def toString(self):
        for cellRow in self.cells:
            for cell in cellRow:
                print(cell.toString())
                print()
                

    def truckHere(self):
        print(f'truck location: {self.trucks[0].location.toString()}')
