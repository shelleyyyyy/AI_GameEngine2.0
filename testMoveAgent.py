from argparse import Action
from moveAgent import MoveAgent
from environment import Environment
from environment import TruckAgent
from moveAgent import MoveAgent
#agent = MoveAgent()

#action = ['north', 'east']

# agent.insertAction(action)
# agent.obtainCosts()
# agent.printCost()

actions = ['north']

e = Environment()

a = MoveAgent(e.trucks[0], e)
a.start(actions)

e.truckHere()