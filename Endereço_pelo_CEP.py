# API do ViaCEP
# passar um CEP e ela retorna as informações
# passar um endereço e retorna um CEP
# https://viacep.com.br/

# Busca endereço a partir de CEP

import requests as r

cep = input("\nDigite o CEP: ")

cep = cep.replace(".","").replace("-","").replace(" ","")

if len(cep) != 8:
    print("\nCEP inválido.")
    
else:
    link = f'https://viacep.com.br/ws/{cep}/json/'
    requisicao = r.get(link)
   # print(requisicao)
    dicionario = requisicao.json()
    
    rua = dicionario['logradouro']
    bairro = dicionario['bairro']
    cidade = dicionario['localidade']
    uf = dicionario['uf']


    print("\n",rua," - ",bairro," - ",cidade,"/",uf)
    