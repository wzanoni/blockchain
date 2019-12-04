# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 14:00:00 2019
@author: washington.zanoni
@email: xdata.science@gmail.com

Descrição:
	Esse código busca/retorna informações do bloco que está na mempool do Blockchain.
	É necessario criar pastas em seu computador
Fonte:
	https://blockchain.info
End-point:
    https://api.blockchair.com/bitcoin/state/changes/mempool

"""
#--------------------------------------------------------------------------------------------------#

# imports
import requests
import pandas as pd
import json
from pandas.io.json import json_normalize

#--------------------------------------------------------------------------------------------------#

# crie diretórios/arquivo c:/blockchain/upblocks_mempool/
''' 
    Nesse diretório será criado e
    salvo os arquivos no formato json
    com o conteúdo do bloco na mempool
'''
path_json  = 'C:/blockchain/upblocks_mempool/'

#--------------------------------------------------------------------------------------------------#

# Daqui para baixo não precisa alterar nada
'''
     o blocoserá salvo no diretório 
     c:/blockchain/upblocks_mempool/      
'''
     
print('Start....')
try:
        url = 'https://api.blockchair.com/bitcoin/state/changes/mempool'
        arq_json = requests.get(url).json()    
        with open(path_json+'block.json', 'a') as json_file:
            json.dump(arq_json, json_file)  
            json_file.close()
except Except as e:       
            print('erro /n', e)
            pass 
print('End...')
