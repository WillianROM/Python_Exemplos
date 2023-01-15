# https://www.youtube.com/watch?v=QkDiBWJ8Row
# Criar o projeto no Firebase - https://firebase.google.com/?hl=pt
# Criar o Database (atenção às regras de segurança)
# Estrutura de árvore
    # Ir em Criar um novo projeto -> Criação -> Realtime Database -> Criar banco de dados -> Próxima -> Iniciar no modo de teste -> Ativar

# Interação com o Database (REST API)

import requests
import json

link = "https://fir-rest-api-48e4a-default-rtdb.firebaseio.com/"


# Criar uma venda (POST)
"""
dados = {
            'cliente':'Mario',
            'preço': 80,
            'produto': 'teclado',
            'quantidade': 1
        } # O body que é enviado na requisão abaixo

requisicao = requests.post(f'{link}/Vendas/.json',data=json.dumps(dados)) # O json.dumps é para converter para o formato json para ser transmitido na re1quisição

print(requisicao)
print(requisicao.json())
print(requisicao.text)
"""

# Criar um novo produto (POST)
"""
dados = {
            'nome':'teclado',
            'preço': 80,
            'quantidade': 10
        } # O body que é enviado na requisão abaixo

requisicao = requests.post(f'{link}/Produtos/.json',data=json.dumps(dados)) # O json.dumps é para converter para o formato json para ser transmitido na re1quisição

print(requisicao)
print(requisicao.json())
print(requisicao.text)
"""

# Editar a venda (PATCH)
"""
dados = {
            'cliente':'Luigi'
        } # O body que é enviado na requisão abaixo

requisicao = requests.patch(f'{link}/Vendas/IDV01/.json',data=json.dumps(dados)) # O json.dumps é para converter para o formato json para ser transmitido na re1quisição

print(requisicao)
print(requisicao.json())
print(requisicao.text)
"""

# Pegar uma venda específico ou todas as vendas (GET)
"""
requisicao = requests.get(f'{link}/.json')
print(requisicao)
dicionario_requisicao = requisicao.json() # .json() transforma em dicionário Python para utilizar

print(dicionario_requisicao['Produtos'])
print(dicionario_requisicao['Vendas'])
"""

requisicao = requests.get(f'{link}/Vendas.json')
#print(requisicao)
dicionario_requisicao = requisicao.json() # .json() transforma em dicionário Python para utilizar

#print(dicionario_requisicao)

for id_venda in dicionario_requisicao:
    cliente = dicionario_requisicao[id_venda]['cliente']
    if cliente == "Mario":
        print(id_venda)
        id_mario = id_venda

# Deletar uma venda (DELETE)
requisicao = requests.delete(f'{link}/Vendas/{id_mario}/.json')
print(requisicao)
print(requisicao.text)

# O que seria de legal após isso?
# Autenticação
# Criar outras estruturas no seu banco de dados (vendedor, loja, cliente, estoque, etc.)
