from gameEngine.cell import Cell
from gameEngine.location import Location
from gameEngine.truckAgent import TruckAgent
from constants import constants
import random

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
        self.root: Cell = Cell()

        self.makeCells()
        self.populateEnv(trucks=self.truckAgentCount, blocks=self.nonPassableCount, goals=self.goalCount)
        #self.populateEnvPreBuilt()
        #self.toString()

    def generateEnvironment(self):
        self.makeCells()


    def makeCells(self):
        for x in range(self.gridSize):
            cellRow: Cell = []
            for y in range(self.gridSize):
                cellRow.append(Cell(x, y))
            self.cells.append(cellRow)

    def check_if_open(self, cell: Cell):
        if cell.cell_type == constants["BLANK"]:
            return True
        else:
            return False

    def populateEnv(self, trucks: int, blocks: int, goals: int):
        for x in range(0, trucks):
            cell: Cell = self.cells[random.randint(0, self.gridSize) - 1][random.randint(0, self.gridSize) - 1]
            while self.check_if_open(cell) == False:
                cell = self.cells[random.randint(0, self.gridSize) - 1][random.randint(0, self.gridSize) - 1]
            cell.cell_type = constants["TRUCK"]
            self.root = cell

        for x in range(0, goals):
            cell = self.cells[random.randint(0, self.gridSize) - 1][random.randint(0, self.gridSize) - 1]
            while self.check_if_open(cell) == False:
                cell = self.cells[random.randint(0, self.gridSize) - 1][random.randint(0, self.gridSize) - 1]
            cell.cell_type = constants["GOAL_CELL"]

        for x in range(0, blocks):
            cell = self.cells[random.randint(0, self.gridSize) - 1][random.randint(0, self.gridSize) - 1]
            while self.check_if_open(cell) == False:
                cell = self.cells[random.randint(0, self.gridSize) - 1][random.randint(0, self.gridSize) - 1]
            cell.cell_type = constants["NON_PASSABLE"]

    
    def populateEnvPreBuilt(self):
        self.cells[0][2].cell_type = (constants["NON_PASSABLE"])
        self.cells[1][3].cell_type = (constants["NON_PASSABLE"])
        self.cells[2][2].cell_type = (constants["NON_PASSABLE"])

        self.cells[2][1].cell_type = (constants["NON_PASSABLE"])
        self.cells[4][3].cell_type = (constants["NON_PASSABLE"])
        self.cells[2][3].cell_type = (constants["TRUCK"])
        self.cells[2][3].truck = TruckAgent(x=2, y=3)
        self.cells[0][0].cell_type = (constants["GOAL_CELL"])
        
        self.trucks.append(self.cells[4][4].cell_type)

    def get_cells_by_type(self):
        cells_type = []
        for row in self.cells:
            cellRow: Cell = []
            for cell in row:
                cellRow.append(cell.cell_type)
            cells_type.append(cellRow)
        return cells_type

    def toString(self):
        for cellRow in self.cells:
            for cell in cellRow:
                print(cell.cell_type, end=" | ")
            print()
                

    def truckHere(self):
        print(f'truck location: {self.trucks[0].location.toString()}')
