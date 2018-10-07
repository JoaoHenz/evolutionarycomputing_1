from antcolony import ant_colony
from simulatedannealing import SimulatedAnnealing
import sys, numpy, random


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
	print('opa que?\n',dataset,'\n\n')
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


print('\nHello!')

print('\nOpening archive:', sys.argv[1])
dataset  = readdataset(sys.argv[1])
print('\nDataset:\n', dataset)
'''
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
'''
print('Bye, bye.\n')
