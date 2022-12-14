from gameEngine.location import Location
from constants import constants
from gameEngine.environment import Environment
from gameEngine.cell import Cell
from Infrastructure.node import Node
from gameEngine.truckAgent import TruckAgent
import math

def hueristics(node: Cell, environment: Environment):

    tl = node.location
    goals: Cell = environment.goals
    hur = -1
    for g in goals:
        x = math.pow((tl.x - g.location.x), 2)
        y = math.pow((tl.y - g.location.y), 2)
        p = math.sqrt(x+y)
        if hur == -1:
            hur.append(g)
        elif hur > p:
            hur = g
        
    return hur