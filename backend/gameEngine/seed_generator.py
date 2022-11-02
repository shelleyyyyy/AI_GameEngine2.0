import random
import math
from gameEngine.cell import Cell
from constants import constants

def generateWhiteNoise(width,height, seed):
    random.seed(seed)
    noise = [[r for r in range(width)] for i in range(height)]

    truck_x, truck_y = random.randint(0, 10), random.randint(0, 10)
    goal_x, goal_y = random.randint(0, 10), random.randint(0, 10)

    for i in range(0,height):
        for j in range(0,width):
            num = random.randint(0,3)

            if i == truck_x and j == truck_y:
                noise[i][j] = Cell(x=i, y=j, cell_type=constants["TRUCK"])
            elif i == goal_x and j == goal_y:
                noise[i][j] = Cell(x=i, y=j, cell_type=constants["GOAL_CELL"])
            elif num == 0:
                noise[i][j] = Cell(x=i, y=j, cell_type=constants["NON_PASSABLE"])
            else:
                noise[i][j] = Cell(x=i, y=j)


    return noise