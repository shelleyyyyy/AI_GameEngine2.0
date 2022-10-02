from location import Location

class Blocked:
    def __init__(self, id):
        self.location = Location()
        self.percept = "****"
        self.id = id

    def toString(self):
        print("Blocked")
        print("ID: ", self.id)
        self.location.toString()
        print("Percept: ", self.percept)
