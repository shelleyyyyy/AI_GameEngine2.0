from location import Location

class Open:
    def __init__(self, id):
        self.location = Location()
        self.percept = "open"
        self.id = id

    def toString(self):
        print("Open")
        print("ID: ", self.id)
        self.location.toString()
        print("Percept: ", self.percept)
