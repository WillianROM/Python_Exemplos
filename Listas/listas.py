# https://www.youtube.com/watch?v=wgGu8ph3m6A
lista_compras = ['banana','maçã','laranja']

print(f'Item da lista na primeira posição [base zero]: {lista_compras[0]}') # Base zero

########################################################################
print(f'Último item da lista na posição [-1]: {lista_compras[-1]}') # Pega o último item

########################################################################
lista_compras.append('abacaxi') # Acrescentar mais um item no fim da lista
print(f'Lista com item adicionado no fim: {lista_compras}')

########################################################################
lista_compras.insert(2,'melância')  # Acrescentar mais um item em alguma posição da lista
print(f'Lista com item adicionado conforme posição informada: {lista_compras}')

########################################################################
del lista_compras[3] # Para excluir algum item da lista conforme a posição
print(f'Lista com um item excluido conforme posição: {lista_compras}')

########################################################################
lista_compras.remove('banana')
print(f'Lista com um item excluido conforme nome do item: {lista_compras}')

########################################################################
lista_compras.append('carro')
print(f'Foi adicionado um item a mais na lista: {lista_compras}')
lista_sonhos = []
sonho = lista_compras.pop(-1) # Vai retirar o último item da lista_compras e colocar na variável sonho
print(sonho)
lista_sonhos.append(sonho)
print(f'Lista depois de usar a função pop: {lista_compras}') 
print(f'Outra lista, lista sonhos: {lista_sonhos}')

########################################################################
tarefas = []
tarefa = input('Insira uma tarefa: ')
tarefas.append(tarefa)

while tarefa != '':
    tarefa = input('Insira uma tarefa: ')
    tarefas.append(tarefa)

print(tarefas[0:-1])

########################################################################
lojas = ['Curitiba','Rio de Janeiro','São Paulo']
faturamento = [8000,5000,9000]

print(lojas)
print(faturamento)

faturamento.sort() # Para ordenar a lista do menor para maior
print(faturamento)

faturamento.sort(reverse = True) # Para ordenar a lista do maior para o menor
print(faturamento)

########################################################################
resultados = []
for i in range(3): # Apesar da base zero, como são 3 itens na lista, então coloque range(3)
    tupla = (lojas[i-1], faturamento[i-1])
    resultados.append(tupla)
print(resultados)
print(resultados[1][1])
