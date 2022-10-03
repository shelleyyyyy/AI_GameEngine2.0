from location import Location

class Open:
    def __init__(self, id=0):
        self.location = Location()
        self.percept = "open"
        self.id = id

    def toString(self):
        print("Open Type")

