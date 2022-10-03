from location import Location

class Blocked:
    def __init__(self, id=0):
        self.location = Location()
        self.percept = "****"
        self.id = id

    def toString(self):
        print("Blocked Type")
