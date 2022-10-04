from argparse import Action
from MoveAgent import MoveAgent
from environment import Environment
from environment import TruckAgent
from MoveAgent import MoveAgent
#agent = MoveAgent()

#action = ['north', 'east']

# agent.insertAction(action)
# agent.obtainCosts()
# agent.printCost()

actions = ['north']

e = Environment()

e.toString()

print()

a = MoveAgent(e.trucks[0], e)
a.start(actions)

e.truckHere()

print()

e.toString()