from location import Location
from open import Open

class Cell:
    def __init__(self, x, y, cellType=Open()):
        self.type = cellType
        self.location = Location(x, y)

    def toString(self):
        print("Cell")
        self.location.toString()
        print("Contains")
        self.type.toString()

    def setType(self, cellType):
        self.type = cellType