from wtapassive import *
import os
import pickle

from result import *

file = open('results_finais','wb')
file.truncate(0)

resultlist = []
for filename in os.listdir('./wta_instances'):
    print('\ncomeçando processamento de ',filename,'.......')
    result = onetest('./wta_instances/'+filename)
    result.filename = filename
    result.testname = 'final'
    resultlist.append(result)
    print('valor do melhor caminho:  ',result.valordocaminho)
    print(':::fim de instância!')

print('\ncomeçando a salvar os resultados.......')
pickle.dump(resultlist,file)
print(':::resultados foram salvos com sucesso!')
