from MoveAgent import MoveAgent
agent = MoveAgent()

action = ['north', 'east']

agent.insertAction(action)
agent.obtainCosts()
agent.printCost()