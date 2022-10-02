import uuid
from location import Location

class TruckAgent:

    def __init__(self, location=Location(), direction=0, percept='unknown', movable=True):
        self.ID = uuid.uuid4()
        self.location = location
        self.direction = direction
        self.percept = percept
        self.movable = movable


    def toString(self):
        print("ID:", self.ID)
        print("location:", self.location)
        print("direction:", self.direction)
        print("percept: " + self.percept)
        print("moveable", self.movable)

if __name__=="__main__":
    truck = TruckAgent()
    truck.toString()
