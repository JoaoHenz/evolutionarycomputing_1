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
		while j<len(dataset) and k<numberofinstances:
			row.append(dataset[j])
			k+=1
			j+=1
		newdataset.append(row)


	return newdataset

def presentResult():
	pass
	#TODO

def makeGraphics():
	pass
	#TODO

def generate_testnodes(dataset):
	test_nodes = {}
	k = 0
	for i in range(1,len(dataset)): #  i=arma, j=alvo
		for j in range(0,len(dataset[0])):
				test_nodes[k]= (dataset[i][j],dataset[0][j],i,j)
				k+=1
	return test_nodes

def distance(start,end,nodes):
	distance = 0
	for key in nodes:

	distance = 
	return distance

print('\nHello!')

print('\nOpening archive:', sys.argv[1])
dataset  = readdataset(sys.argv[1])
print('\ndataset:\n',dataset,'\n')

alpha = float(sys.argv[2])
beta = float(sys.argv[3])
ant_count = int(sys.argv[4])

print('\nAnt Colony:')
test_nodes = generate_testnodes(dataset)
print('\ntestnodes:\n',test_nodes,'\n')
colony = ant_colony(test_nodes,distance,alpha= alpha, beta = beta, ant_count= ant_count ,iterations = 5,target_count = numberofinstances)
answer = colony.mainloop()

'''
print('\nSimulated Annealing:')
result = SM_Metaheuristic(data)
presentResult(result)
print('continue and make graphic?')
makeGraphics()
'''
print('Bye, bye.\n')
