from wtapassive import *
import os
import pickle

from result import *




# alpha, beta, ant_count, pheromone_evaporation_coefficient, pheromone_constant
variacoes = [[ 0.75,0.25, 1.0],[ 1.0, 1.8, 2.4],[10, 25,80],[10, 100,40],[.10, .90,.60],[2500.0,500.0,1500.0]]
file = open('results','wb')
file.truncate(0)

resultlist = []
for filename in os.listdir('./wta_instances'):
    if filename == 'wta30.txt' or filename == 'wta20.txt':
        print('\ncomeçando processamento de ',filename,'.......')
        for i in range(len(variacoes[0])):
            result = onetest('./wta_instances/'+filename,alpha= variacoes[0][i])
            result.filename = filename
            resultlist.append(result)
            print(':::fim de instância!')
        for i in range(len(variacoes[1])):
            result = onetest('./wta_instances/'+filename,beta= variacoes[1][i])
            result.filename = filename
            resultlist.append(result)
            print(':::fim de instância!')
        for i in range(len(variacoes[2])):
            result = onetest('./wta_instances/'+filename,ant_count= variacoes[2][i])
            result.filename = filename
            resultlist.append(result)
            print(':::fim de instância!')
        for i in range(len(variacoes[3])):
            result = onetest('./wta_instances/'+filename,iterations= variacoes[3][i])
            result.filename = filename
            resultlist.append(result)
            print(':::fim de instância!')
        for i in range(len(variacoes[4])):
            result = onetest('./wta_instances/'+filename,pheromone_evaporation_coefficient= variacoes[4][i])
            result.filename = filename
            resultlist.append(result)
            print(':::fim de instância!')
        for i in range(len(variacoes[5])):
            result = onetest('./wta_instances/'+filename,pheromone_constant= variacoes[5][i])
            result.filename = filename
            resultlist.append(result)
            print(':::fim de instância!')

print('\ncomeçando a salvar os resultados.......')
pickle.dump(resultlist,file)
print(':::resultados foram salvos com sucesso!')
