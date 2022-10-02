from location import Location
import uuid

class Goal:

    def __init__(self, location=Location(), percept="unknown", found=False):
        self.ID = uuid.uuid4()
        self.location = location
        self.percept = percept
        self.found = found
    
    def toString(self):
        print("ID:", self.ID)
        print("location:", self.location.toString())
        print("percept: " + self.percept)
        print("found:", self.found)

if __name__=="__main__":
    goal = Goal()
    goal.toString()

