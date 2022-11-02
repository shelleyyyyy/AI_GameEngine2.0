import random
import math
from gameEngine.cell import Cell
from constants import Constants

def generateWhiteNoise(width,height, seed):
    random.seed(seed)
    noise = [[r for r in range(width)] for i in range(height)]

    for i in range(0,height):
        for j in range(0,width):
            num = random.randint(0,3)
            if num == 0:
                noise[i][j] = Cell(x=i, y=j, cell_type=constants["NON_PASSABLE"])
            else:
                noise[i][j] = Cell(x=i, y=j)


    return noise