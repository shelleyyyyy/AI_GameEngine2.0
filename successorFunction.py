import collections
from location import Location
from constants import constants
from node import Node
  
class SuccessorFunction:
    def __init__(self):
        pass

    def goForward(self, environment, state):

        shiftXValue = 0
        shiftYValue = 0

        if state.direction == FACING_SOUTH:
            shiftXValue = MOVING_SOUTH
        elif state.direction == FACING_WEST:
            shiftYValue = MOVING_WEST
        elif state.direction == MOVING_NORTH:
            shiftXValue = MOVING_NORTH
        else:
            shiftYValue = MOVING_EAST

        i = state.location.x + shiftXValue
        j = state.location.y + shiftXValue

        if i < 0 or i >= len(environment.trucks) or j < 0 or j >= len(environment.trucks):
            return False

    def turnRight(self, state):
        pass
    def turnLeft(self, state):
        pass

    def expand(self, node, environment):
        list = collections.deque()

        parentNode = node.copyOfNode()

        try:
            list.append(SuccessorFunction(parentNode, constants["GO_FORWARD"], environment))
        except:
            pass

        parentNode = node.copyOfNode()
        list.append(SuccessorFunction(parentNode, GO_RIGHT, environment))
        parentNode = node.copyOfNode()
        list.append(SuccessorFunction(parentNode, GO_LEFT, environment))

        return list

    def successorFunction(self, parent, action, environment):
        state = parent.state.type #state is a Cell Type

        shiftXValue = 0
        shiftYValue = 0

        if state.direction == constants['FACING_SOUTH']:
            shiftXValue = constants['MOVING_SOUTH']
        elif state.direction == constants['FACING_WEST']:
            shiftYValue = constants['MOVING_WEST']
        elif state.direction == constants['MOVING_NORTH']:
            shiftXValue = constants['MOVING_NORTH']
        else:
            shiftYValue = constants['MOVING_EAST']
        
        if action == constants['GO_FORWARD']:
            if self.goForward(environment, state):
                i = state.location.x + shiftXValue
                j = state.location.y + shiftYValue

                if i < 0 or i >= len(environment.trucks) or j < 0 or j >= len(environment.trucks):
                    return None
                
                #potentially need to set the percepts of the cell it moves to 
                state.location = Location(i, j)
            else:
                return None
        elif action == TURN_RIGHT:
            self.turnRight(state)
        elif action == TURN_LEFT:
            self.turnLeft(state)
        else:
            pass

        node = Node(state=state, parent=parent, action=action)
        return node

    