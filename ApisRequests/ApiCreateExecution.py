import requests # pip install requests

requisicao = requests.get('https://minhaprimeiraapi.willianmelo1.repl.co/pegarvendas')

print(requisicao) # Para ver o status da requisição, por exemplo 200
print(requisicao.json()) # Para ver o corpo do response em formato json
