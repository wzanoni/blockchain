# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 14:26:43 2019
@author: washington.zanoni

Descrição:
Esse código busca/retorna blocos especificando uma faixa de números dos blocos.
É necessario criar pastas em seu computador

Fonte:
https://blockchain.info

End-point:
    https://blockchain.info/block-height/{numero-bloco}?format=json
"""



import requests
import pandas as pd
import json
from pandas.io.json import json_normalize
from IPython.display import display

# crie diretórios/arquivo c:/blockchain/upblocks_range/
path_json  = 'C:/blockchain/upblocks_range/'
cont_block = 3
i=0

print('Start....')
while i <= cont_block:
    try:
        url = 'https://blockchain.info/block-height/'+str(i)+'?format=json'
        arq_json = requests.get(url).json()    
        with open(path_json+str(i)+'blocks.json', 'w') as json_file:
            json.dump(arq_json, json_file)  
            json_file.close()
        print(i)  
        i=i+1  
        time.sleep(10)
    except Except as e:       
            i=i-1
            print('erro', i , ' /n', e)
            pass 
print('End...')