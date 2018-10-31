from wtapassive import *
import os
import pickle
import statistics

from result import *



# 0.5 1.2 50 80 1000.0
# alpha, beta, ant_count, iterations, pheromone_evaporation_coefficient, pheromone_constant
variacoes = [
    [.1,.2,.3,.4,.5,.6,.7,.8,.9,1.1,1.2,1.3,1.4,1.5,1.6,1.7,1.8],
    [1.0,1.2,1.4,1.6,1.8,2.0,2.2,2.4,2.6,2.8,3.0,3.2,3.4,3.6,3.8,4.0,4.2,4.4],
    [10,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180],
    [10,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180],
    [.1,.15,.2,.25,.3,.35,.4,.45,.5,.55,.6,.65,.7,.75,.8,.85,.9,.95],
    [200.0,400.0,600.0,800.0,1000.0,1200.0,1400.0,1600.0,1800.0,2000.0,2200.0,2400.0,2600.0,2800.0,3000.0,3200.0,3400.0,3600.0]
]
file = open('results2','wb')
file.truncate(0)
med_len = 15
resultlist = []
for filename in os.listdir('./wta_instances'):
    if filename == 'awta5.txt':
        print('\ncomeçando processamento de ',filename,'.......')

        print(':::alpha')
        for i in range(len(variacoes[0])):
            med_lista = []
            for j in range(med_len):
                result = onetest('./wta_instances/'+filename,alpha= variacoes[0][i])
                result.filename = filename
                result.testname = 'alpha'
                med_lista.append(result)
                print('alpha:',result.valordocaminho)
            print(':::fim de instância!')
            result = med_lista[0]
            result.valordocaminho = sum(x.valordocaminho for x in med_lista)/med_len
            result.standarddeviation = statistics.stdev(x.valordocaminho for x in med_lista)
            print('valor do alpha:',result.alpha)
            resultlist.append(result)
            print('média do alpha:',result.valordocaminho)

        print(':::beta')
        for i in range(len(variacoes[1])):
            med_lista = []
            for j in range(med_len):
                result = onetest('./wta_instances/'+filename,beta= variacoes[1][i])
                result.filename = filename
                result.testname = 'beta'
                med_lista.append(result)
            print(':::fim de instância!')
            result = med_lista[0]
            result.valordocaminho = sum(x.valordocaminho for x in med_lista)/med_len
            result.standarddeviation = statistics.stdev(x.valordocaminho for x in med_lista)
            resultlist.append(result)

        print(':::ant_count')
        for i in range(len(variacoes[2])):
            med_lista = []
            for j in range(med_len):
                result = onetest('./wta_instances/'+filename,ant_count= variacoes[2][i])
                result.filename = filename
                result.testname = 'ant_count'
                med_lista.append(result)
            print(':::fim de instância!')
            result = med_lista[0]
            result.valordocaminho = sum(x.valordocaminho for x in med_lista)/med_len
            result.standarddeviation = statistics.stdev(x.valordocaminho for x in med_lista)
            resultlist.append(result)

        print(':::iterations')
        for i in range(len(variacoes[3])):
            med_lista = []
            for j in range(med_len):
                result = onetest('./wta_instances/'+filename,iterations= variacoes[3][i])
                result.filename = filename
                result.testname = 'iterations'
                med_lista.append(result)
            print(':::fim de instância!')
            result = med_lista[0]
            result.valordocaminho = sum(x.valordocaminho for x in med_lista)/med_len
            result.standarddeviation = statistics.stdev(x.valordocaminho for x in med_lista)
            resultlist.append(result)

        print(':::pheromone_evaporation_coefficient')
        for i in range(len(variacoes[4])):
            med_lista = []
            for j in range(med_len):
                result = onetest('./wta_instances/'+filename,pheromone_evaporation_coefficient= variacoes[4][i])
                result.filename = filename
                result.testname = 'pheromone_evaporation_coefficient'
                med_lista.append(result)
            print(':::fim de instância!')
            result = med_lista[0]
            result.valordocaminho = sum(x.valordocaminho for x in med_lista)/med_len
            result.standarddeviation = statistics.stdev(x.valordocaminho for x in med_lista)
            resultlist.append(result)

        print(':::pheromone_constant')
        for i in range(len(variacoes[5])):
            med_lista = []
            for j in range(med_len):
                result = onetest('./wta_instances/'+filename,pheromone_constant= variacoes[5][i])
                result.filename = filename
                result.testname = 'pheromone_constant'
                med_lista.append(result)
            print(':::fim de instância!')
            result = med_lista[0]
            result.valordocaminho = sum(x.valordocaminho for x in med_lista)/med_len
            result.standarddeviation = statistics.stdev(x.valordocaminho for x in med_lista)
            resultlist.append(result)

print('\ncomeçando a salvar os resultados.......')
pickle.dump(resultlist,file)
print(':::resultados foram salvos com sucesso!')
