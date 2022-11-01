from environment import Environment
from searchAlgorithms.uniformed_cost_search import uniformed_cost_search

e = Environment()

s = uniformed_cost_search(e,e.cells[2][3])

print(s)