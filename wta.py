


from antcolony.py import ant_colony
from simulatedannealing.py import SimulatedAnnealing



def open():
pass
#TODO

def presentResult():
pass
#TODO	

def makeGraphics():
pass
#TODO
	



print('\nHello!')

print('\nOpening archive:')
data  = open()

print('\nAnt Colony:')
result = antcolonyMetaheuristic(data)
presentResult(result)
print('continue and make graphic?')
makeGraphics()

print('\nSimulated Annealing:')
result = SM_Metaheuristic(data)
presentResult(result)
print('continue and make graphic?')
makeGraphics()

print('Bye, bye.\n')
	

