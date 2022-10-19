from cell import Cell
from location import Location
from truckAgent import TruckAgent
from constants import constants

class Environment:
    def __init__(self, gridSize=5, nonPassableCount=5, truckAgentCount=1, goalCount=1):
        self.gridSize = gridSize
        self.cells: Cell = []
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
            cellRow: Cell = []
            for y in range(self.gridSize):
                cellRow.append(Cell(x, y))
            self.cells.append(cellRow)
    
    def populateEnv(self):
        self.cells[0][2].cell_type = (constants["NON_PASSABLE"])
        self.cells[1][3].cell_type = (constants["NON_PASSABLE"])
        self.cells[2][2].cell_type = (constants["NON_PASSABLE"])

        self.cells[2][1].cell_type = (constants["NON_PASSABLE"])
        self.cells[4][3].cell_type = (constants["NON_PASSABLE"])
        self.cells[2][3].cell_type = (constants["TRUCK"])
        self.cells[2][3].truck = TruckAgent(x=2, y=3)
        self.cells[3][3].cell_type = (constants["GOAL_CELL"])
        
        self.trucks.append(self.cells[4][4].cell_type)

    def toString(self):
        for cellRow in self.cells:
            for cell in cellRow:
                print(cell.toString())
                print()
                

    def truckHere(self):
        print(f'truck location: {self.trucks[0].location.toString()}')
