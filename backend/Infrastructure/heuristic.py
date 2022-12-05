from gameEngine.location import Location
from constants import constants
from gameEngine.environment import Environment
from gameEngine.cell import Cell
from Infrastructure.node import Node
from gameEngine.truckAgent import TruckAgent
import math

class Heuristics():

    def __init__(self):
        pass
        
    def start_hueristic(truck: TruckAgent, environment: Environment):

        tl = truck.location
        goals: Cell = environment.goals
        hur = []
        for g in goals:
            x = math.pow((tl.x - g.location.x), 2)
            y = math.pow((tl.y - g.location.y), 2)
            p = math.sqrt(x+y)
            if g.found == True:
                continue
            if len(hur) != 0:
                hur.append(g)
            elif hur[0] > p:
                hur.insert(0, g)
            else:
                hur.append(g)

        return hur

    def check_if_found(hur):
        if hur[0].found == True:
           hur.pop()
        return(hur)

    def check_heuristic(truck: TruckAgent, goal: Cell):
        x = math.pow((truck.location.x - goal.location.x), 2)
        y = math.pow((truck.location.y - goal.location.y), 2)
        p = math.sqrt(x+y)
        
        return p