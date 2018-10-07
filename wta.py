from antcolony import ant_colony
from simulatedannealing import SimulatedAnnealing
import sys, numpy, random


numberofinstances = 0

def readdataset(datasetpath):
	dataset = []
	file = open(datasetpath,'r')

	for line in file:
		dataset.append(float(line))


	return fixdataset(dataset)

def fixdataset(dataset):
	newdataset = []
	numberofinstances = int(dataset[0])
	j = 1
	row = []
	for i in range(0,numberofinstances):
		row.append(dataset[j])
		j+=1
	newdataset.append(row)

	i=1
	while j < len(dataset):
		row =[]
		k=0
		while j+k<len(dataset) and k<numberofinstances:
			row.append(dataset[j])
			k+=1
			j+=1
		newdataset.append(row)
		j+=1

	print('opa que?\n',newdataset,'\n\n')
	newdataset = numpy.matrix(newdataset)
	return newdataset

def presentResult():
	pass
	#TODO

def makeGraphics():
	pass
	#TODO


generate_testnodes(dataset):
	test_nodes = {}
	for i in range(0,numberofinstances):
		test_nodes[i] = dataset[:,i]
	return test_nodes

def distance(start,end):


print('\nHello!')

print('\nOpening archive:', sys.argv[1])
dataset  = readdataset(sys.argv[1])

print('\nAnt Colony:')
test_nodes = generate_testnodes(dataset)
colony = ant_colony(test_nodes,distance)
answer = colony.mainloop()

'''
print('\nSimulated Annealing:')
result = SM_Metaheuristic(data)
presentResult(result)
print('continue and make graphic?')
makeGraphics()
'''
print('Bye, bye.\n')
