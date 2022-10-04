costN = 1
costS = 1
costE = 1
costW = 1

def getCosts(action):
    if action == 'north':
        return costN
    elif action == 'south':
        return costS
    elif action == 'west':
        return costW
    elif action == 'east':
        return costE
    return 'incorrect input'

