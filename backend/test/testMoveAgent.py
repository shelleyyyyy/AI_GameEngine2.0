from argparse import Action
from moveAgent import MoveAgent
from gameEngine.environment import Environment
from gameEngine.environment import TruckAgent
from moveAgent import MoveAgent
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