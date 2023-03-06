import requests as r
import pprint as pp

uf = input("Digite o UF: ")
cidade = input("Digite a cidade: ")
endereco = input("Digite a rua: ")

link = f'https://viacep.com.br/ws/{uf}/{cidade}/{endereco}/json/'

requisicao = r.get(link)
dicionario = requisicao.json()
pp.pprint(dicionario)