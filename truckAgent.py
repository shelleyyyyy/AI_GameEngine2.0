import uuid
from Location import Location

class TruckAgent:

    def __init__(self, location=Location(), direction="unknown", percept='unknown'):
        self.ID = uuid.uuid4()
        self.location = location
        self.direction = direction
        self.percept = percept

    def toString(self):
        print("ID: " + str(self.ID))
        print("location: " + self.location)
        print("direction: " + self.direction)
        print("percept: " + self.percept)

if __name__=="__main__":
    truck = TruckAgent()
    truck.toString()
