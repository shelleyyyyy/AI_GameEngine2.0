import collections
from location import Location
from constants import constants
from environment import Environment
from cell import Cell
from node import Node
  
class SuccessorFunction:
    def __init__(self):
        pass

    def goForward(self, environment: Environment, state: Cell):

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

        i = state.location.x + shiftXValue
        j = state.location.y + shiftYValue

        if i < 0 or i > environment.gridSize - 1 or j < 0 or j > environment.gridSize - 1:
            return False
        elif environment.cells[i][j].cell_type == constants['NON_PASSABLE']:
            return False
        else:
            return True

    def turnRight(self, state: Cell):
        state.direction = abs((state.direction + 1) % 4)
        
    def turnLeft(self, state: Cell):
        state.direction = abs((state.direction - 1 + 4) % 4)
    
    def successorFunction(self, parent: Node, action, environment: Environment):
        copy_of_parent = parent.copyOfNode()
        state = copy_of_parent.state

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
                
                #grab existing cell from cells array
                state.location = Location(i, j)
            else:
                return None
        elif action == constants['TURN_RIGHT']:
            self.turnRight(state)
        elif action == constants['TURN_LEFT']:
            self.turnLeft(state)
        else:
            pass
    
        parent.actionsList.append(action)
        updated_action_list = parent.actionsList
        node = Node(state=state, parent=parent, action=action, actionsList=updated_action_list)
        return node

    def expand(self, node: Node, environment: Environment):
        list = collections.deque()

        parentNode = node.copyOfNode()

        forward = self.successorFunction(parent=parentNode, action=constants["GO_FORWARD"], environment=environment)
        if forward == None:
            pass
        else:
            list.append(forward)

        parentNode = node.copyOfNode()
        list.append(self.successorFunction(parent=parentNode, action=constants['TURN_RIGHT'], environment=environment))
        parentNode = node.copyOfNode()
        list.append(self.successorFunction(parent=parentNode, action=constants['TURN_LEFT'], environment=environment))

        return list


    