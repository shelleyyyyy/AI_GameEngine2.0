import random
import math
from gameEngine.cell import Cell
from constants import constants
from gameEngine.location import Location
from gameEngine.truckAgent import TruckAgent

def generate_truck_locations(trucks, width, height):
    trucks_locations = {}
    for truck in range(0, trucks):
        t = (truck_x, truck_y) = random.randint(0, width - 1), random.randint(0, height - 1)
        trucks_locations[t] = TruckAgent(x=truck_x, y=truck_y)
    return trucks_locations

def generate_goal_locations(goals, width, height):
    goals_locations = {}
    for goal in range(0, goals):
        g = (goal_x, goal_y) = random.randint(0, width - 1), random.randint(0, height - 1)
        goals_locations[g] = Location(x=goal_x, y=goal_y)
    return goals_locations

def generateWhiteNoise(width,height, seed, root, trucks, goals):
    random.seed(seed)
    noise = [[r for r in range(width)] for i in range(height)]
    
    truck_locations = generate_truck_locations(trucks=trucks, width=width, height=height)
    goal_locations = generate_goal_locations(goals=goals, width=width, height=height)

    root_nodes: Cell = []
    for i in range(0,height):
        for j in range(0,width):
            num = random.randint(0,3)
            if (i, j) in truck_locations:
                truck_cell = Cell(x=i, y=j, cell_type=constants["TRUCK"])
                root_nodes.append(truck_cell)
                noise[i][j] = truck_cell
            elif (i, j) in goal_locations:
                noise[i][j] = Cell(x=i, y=j, cell_type=constants["GOAL_CELL"])
            elif num == 0:
                noise[i][j] = Cell(x=i, y=j, cell_type=constants["NON_PASSABLE"])
            else:
                noise[i][j] = Cell(x=i, y=j)

    return noise, root_nodes
