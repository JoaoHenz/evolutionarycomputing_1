from wtapassive import *
import os
import pickle

from result import *



# 0.5 1.2 50 80 1000.0
# alpha, beta, ant_count, iterations, pheromone_evaporation_coefficient, pheromone_constant
variacoes = [
    [.1,.2,.3,.4,.5,.6,.7,.8,.9],
    [1.0,1.2,1.4,1.6,1.8,2.0,2.2,2.4,2.6],
    [10,20,30,40,50,60,70,80,90],
    [10,20,30,40,50,60,70,80,90],
    [.1,.2,.3,.4,.5,.6,.7,.8,.9],
    [200.0,400.0,600.0,800.0,1000.0,1200.0,1400.0,1600.0,1800.0]
]
file = open('results2','wb')
file.truncate(0)

resultlist = []
for filename in os.listdir('./wta_instances'):
    if filename == 'wta20.txt':
        print('\ncomeçando processamento de ',filename,'.......')
        print(':::alpha')
        for i in range(len(variacoes[0])):
            result = onetest('./wta_instances/'+filename,alpha= variacoes[0][i])
            result.filename = filename
            result.testname = 'alpha'
            resultlist.append(result)
            print(':::fim de instância!')
        print(':::beta')
        for i in range(len(variacoes[1])):
            result = onetest('./wta_instances/'+filename,beta= variacoes[1][i])
            result.filename = filename
            result.testname = 'beta'
            resultlist.append(result)
            print(':::fim de instância!')
        print(':::ant_count')
        for i in range(len(variacoes[2])):
            result = onetest('./wta_instances/'+filename,ant_count= variacoes[2][i])
            result.filename = filename
            result.testname = 'ant_count'
            resultlist.append(result)
            print(':::fim de instância!')
        print(':::iterations')
        for i in range(len(variacoes[3])):
            result = onetest('./wta_instances/'+filename,iterations= variacoes[3][i])
            result.filename = filename
            result.testname = 'iterations'
            resultlist.append(result)
            print(':::fim de instância!')
        print(':::pheromone_evaporation_coefficient')
        for i in range(len(variacoes[4])):
            result = onetest('./wta_instances/'+filename,pheromone_evaporation_coefficient= variacoes[4][i])
            result.filename = filename
            result.testname = 'pheromone_evaporation_coefficient'
            resultlist.append(result)
            print(':::fim de instância!')
        print(':::pheromone_constant')
        for i in range(len(variacoes[5])):
            result = onetest('./wta_instances/'+filename,pheromone_constant= variacoes[5][i])
            result.filename = filename
            result.testname = 'pheromone_constant'
            resultlist.append(result)
            print(':::fim de instância!')

print('\ncomeçando a salvar os resultados.......')
pickle.dump(resultlist,file)
print(':::resultados foram salvos com sucesso!')
