from location import Location
from percept import Percept
from constants import constants
from open import Open

class Cell:
    def __init__(self, x, y, direction, containsTruck=False, blocked=False, cell_type=constants.BLANK, percepts=Percept()):
        self.location = Location(x, y)
        self.direction = direction
        self.cell_type = cell_type
        self.containsTruck = truck
        self.percepts = percept

    def toString(self):
        print("----------Cell----------")
        self.location.toString()
        print("Contains: ", self.type.toString())

    def setType(self, cellType):
        self.type = cellType