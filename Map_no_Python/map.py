# https://www.youtube.com/watch?v=GEciIuxcWkg
# map -> aplica uma função em cada item de uma lista de itens

# Exemplo:
precos = [1000, 1500, 1250, 2500]

def adicionar_imposto(preco):
    return preco * 1.1

# Jeito manual: usando for
precos_com_imposto = []
for preco in precos:
    precos_com_imposto.append(adicionar_imposto(preco))
print(precos_com_imposto)

# usando o map:
precos_com_imposto2 = list(map(adicionar_imposto, precos)) # map(FUNÇÃO, LISTA), coloque o map dentro de um list
print(precos_com_imposto2)

# Aplicação:
# Vamos calcular o preço com imposto em uma base de dados Python:
# Base Vendas.xlsx


