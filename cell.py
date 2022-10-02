from location import Location

class Cell:
    def __init__(self):
        self.type = None
        self.location = Location()

    def toString(self):
        print("Cell")
        self.location.toString()
        print("Contains")
        self.type.toString()

    def setType(self, type):
        self.type = type