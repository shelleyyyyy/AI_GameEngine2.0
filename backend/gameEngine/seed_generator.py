import random
import math

def generateWhiteNoise(width,height, seed):
    random.seed(seed)
    noise = [[r for r in range(width)] for i in range(height)]

    for i in range(0,height):
        for j in range(0,width):
            num = random.randint(0,3)
            if num == 0:
                noise[i][j] = 1
            else:
                noise[i][j] = 0


    return noise