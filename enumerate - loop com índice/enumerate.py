# https://www.youtube.com/watch?v=5IysC0Yjrrg
# enumerate Python

# Obs: usamos quando queremos pegar o índice de um item ao mesmo tempo que queremos o valor do item
vendedores = ["Marcus", "Amanda", "Ale", "Carol"]
vendas = [15, 20, 10, 30]

tamanho_lista = len(vendedores)

for i in range(tamanho_lista):
    print(vendedores[i], vendas[i])



print("#" * 20)

for i, vendedor in enumerate(vendedores):
    print(vendedor, vendas[i])



print("#" * 20)

for vendedor, venda in zip(vendedores, vendas):
    print(vendedor, venda)
