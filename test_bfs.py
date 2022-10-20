
from environment import Environment
from searchAlgorithms.bsf_Cam import breadthFirstSearch

e = Environment()

s = breadthFirstSearch(e,e.cells[2][3])

print(s)