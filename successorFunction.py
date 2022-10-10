import collections
from location import Location
from node import Node
  
class SuccessorFunction:
    def __init__(self):
        pass

    def expand(self, node, environment):
        list = collections.deque()

        parentNode = node.copyOfNode()

        try:
            list.append(SuccessorFunction(parentNode, GO_FORWARD, environment))
        except:
            pass

        parentNode = node.copyOfNode()
        list.append(SuccessorFunction(parentNode, GO_RIGHT, environment))
        parentNode = node.copyOfNode()
        list.append(SuccessorFunction(parentNode, GO_LEFT, environment))

        return list

    def successorFunction(self, parent, action, environment):
        state = parent.state #state is a Cell Type

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
        
        if action == GO_FORWARD:
            if goForward(environment, state):
                i = state.location.x + shiftXValue
                j = state.location.y + shiftXValue

                if i < 0 or i >= len(environment.trucks) or j < 0 or j >= len(environment.trucks):
                    return None
                
                #potentially need to set the percepts of the cell it moves to 
                state.location = Location(i, j)
            else:
                return None
        elif action == TURN_RIGHT:
            turnRight(state)
        elif action == TURN_LEFT:
            turnLeft(state)
        else:
            pass

        node = Node(state=state, parent=parent, action=action)
        return node

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