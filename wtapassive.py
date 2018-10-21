from antcolony import ant_colony
from simulatedannealing import SimulatedAnnealing
import sys, numpy, random
from pylab import figure, axes, pie, title, show
import matplotlib.pyplot as plt
from result import *

global numberofinstances
numberofinstances = 0


def readdataset(datasetpath):
	dataset = []
	file = open(datasetpath,'r')

	for line in file:
		dataset.append(float(line))


	return fixdataset(dataset)

def fixdataset(dataset):
	global numberofinstances
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
	for i in range(1,len(dataset)): # (prob_de_acerto, valor_alvo ,arma ,alvo)
		for j in range(0,len(dataset[0])):
				test_nodes[k]= (dataset[i][j],dataset[0][j],i,j)
				k+=1
	return test_nodes

def distance(start,end,nodes,probvalue_list):
	global targets_value
	global counter
	distance_probability = [1]*numberofinstances

	distance_probability[start[3]] *= (1 - start[0])
	distance_probability[end[3]] *= (1 - end[0])

	distance = 0

	if len(probvalue_list) == 0: #lista recem criada
		for i in range(numberofinstances):
			probvalue_list.append(distance_probability[i] * targets_value[i])
	else: #lista ja existe
		probvalue_list[start[3]] = distance_probability[start[3]] * targets_value[start[3]]
		probvalue_list[end[3]] = distance_probability[end[3]] * targets_value[end[3]]


	distance = sum(probvalue_list)

	return distance

def onetest(datasetpath,alpha=0.5,beta=1.2,ant_count=50,iterations=40,pheromone_evaporation_coefficient=.40,pheromone_constant = 1000.0):
    #print ('\nHello!')
    dataset  = readdataset(datasetpath)
    #print ('\nAnt Colony:')
    #print ('\talpha=', alpha, ', beta=', beta, 'ant_count=', ant_count, 'iterations=', iterations)
    test_nodes = generate_testnodes(dataset)
    global targets_value
    targets_value = [dataset[0][i] for i in range(numberofinstances)]
    # Valor dos alvos
    colony = ant_colony(test_nodes,distance,alpha= alpha, beta = beta, ant_count= ant_count ,iterations = iterations,target_count = numberofinstances,pheromone_evaporation_coefficient= pheromone_evaporation_coefficient, pheromone_constant =pheromone_constant )
    answer = colony.mainloop()
    # Vetor das probabilidades de destruicao acumuladas de cada alvo
    targets_probability = [1]*numberofinstances
    #print ('\nTestnodes:', len(test_nodes))
    for i, node in test_nodes.items():
        if i in answer:
            # Acumula a probabilidade de sobrevivencia
            targets_probability[node[3]] *= (1 - node[0])
    answer_value = 0
    for i in range(numberofinstances):
        answer_value += targets_probability[i] * targets_value[i]
    #print ('\nMenor caminho: ', answer)
    #print ('Valor do caminho: ', answer_value)
    #print('\nBye, bye.\n')
    return Result(answer,answer_value,alpha,beta,ant_count,iterations,pheromone_evaporation_coefficient,pheromone_constant)
