from wtapassive import *
import os
import pickle
#usado para criar a tabela de comparacao com o artigo
from result import *

file = open('results_finais','wb')
file.truncate(0)
filename_list = []
resultlist = []
for filename in os.listdir('./wta_instances'):
    if filename[1:4] =='wta':
        filename_list.append(filename)
    else:
        print(filename[1:3])

filename_list.sort()
print(filename_list)
for filename in filename_list:
    if filename == 'bwta10.txt':
        print('\ncomeçando processamento de ',filename[1:],'.......')
        result = onetest('./wta_instances/'+filename)
        result.filename = filename
        result.testname = 'final'
        resultlist.append(result)
        print('valor do melhor caminho:  ',result.valordocaminho)
        print(':::fim de instância!')

print('\ncomeçando a salvar os resultados.......')
pickle.dump(resultlist,file)
print(':::resultados foram salvos com sucesso!')
