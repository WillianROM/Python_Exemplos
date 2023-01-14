import requests # pip install requests

requisicao = requests.get('https://minhaprimeiraapi.willianmelo1.repl.co/pegarvendas')

dicionario = requisicao.json()

print(requisicao) # Para ver o status da requisição, por exemplo 200
print(dicionario) # Para ver o corpo do response em formato json

print(dicionario['total vendas'])

