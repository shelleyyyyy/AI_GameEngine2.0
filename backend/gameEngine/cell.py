from gameEngine.location import Location
from gameEngine.percept import Percept
from constants import constants
from gameEngine.truckAgent import TruckAgent


class Cell:
    def __init__(self, x=0, y=0, direction=constants['FACING_SOUTH'], truck=TruckAgent(), cell_type=constants['BLANK'], percepts=Percept()):
        self.location: Location = Location(x, y)
        self.direction = direction
        self.cell_type = cell_type
        self.truck: TruckAgent = truck
        self.percepts = percepts
        self.found: bool = False

    def toString(self):
        print("----------Cell----------")
        self.location.toString()
        print("Contains: ", self.cell_type)

    def setType(self, cellType):
        self.type = cellType

    def set_found(self, input: bool):
        self.found = input
    
    def get_found(self):
        return self.found