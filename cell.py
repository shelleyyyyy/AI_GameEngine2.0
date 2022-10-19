from location import Location
from percept import Percept
from constants import constants


class Cell:
    def __init__(self, x, y, direction=constants['FACING_EAST'], containsTruck=False, cell_type=constants['BLANK'], percepts=Percept()):
        self.location: Location = Location(x, y)
        self.direction = direction
        self.cell_type = cell_type
        self.containsTruck = containsTruck
        self.percepts = percepts

    def toString(self):
        print("----------Cell----------")
        self.location.toString()
        print("Contains: ", self.cell_type)

    def setType(self, cellType):
        self.type = cellType