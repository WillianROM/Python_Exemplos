# Observação: o nome desse arquivo não pode ser requests.py, senão vai dá o erro " AttributeError: partially initialized module 'requests' has no attribute 'get' (most likely due to a circular import) "

# Aula: https://www.youtube.com/watch?v=IdviYZIQLlA
# Sites para treinar: https://docs.awesomeapi.com.br/api-de-moedas | https://reqres.in/

# pip install requests
import requests
"""
requisicao = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')
print(requisicao) # Para ver o status da requisição, por exemplo 200
print(requisicao.json()) # Para ver o corpo do response em formato json
"""
# https://testerequisicaodeapis-default-rtdb.firebaseio.com # Criei no Firebase conforme instruído na aula
# No Firebase tem que colocar .json no final do endpoint


# GET

requisicao = requests.get('https://testerequisicaodeapis-default-rtdb.firebaseio.com/.json')
print(requisicao) # Para ver o status da requisição, por exemplo 200
print(requisicao.json()) # Para ver o corpo do response em formato json


# POST

informacoes = '{"Filme": "Mario Bros"}'
requisicao = requests.post('https://testerequisicaodeapis-default-rtdb.firebaseio.com/.json', data=informacoes)
print(requisicao) # Para ver o status da requisição, por exemplo 200
print(requisicao.json()) # Para ver o corpo do response em formato json


# PATCH ou PUT

informacoes = '{"Filme": "Sonic"}'
requisicao = requests.patch('https://testerequisicaodeapis-default-rtdb.firebaseio.com/-NLlBtABHQF-y7dv8Dyy.json', data=informacoes)
print(requisicao) # Para ver o status da requisição, por exemplo 200
print(requisicao.json()) # Para ver o corpo do response em formato json


# DELETE

requisicao = requests.delete('https://testerequisicaodeapis-default-rtdb.firebaseio.com/-NLlBtABHQF-y7dv8Dyy/-NLlFMun7APuMFCKYFl6.json')
print(requisicao) # Para ver o status da requisição, por exemplo 200
print(requisicao.json()) # Para ver o corpo do response em formato json
