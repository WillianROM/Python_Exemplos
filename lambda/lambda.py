# https://www.youtube.com/watch?v=xmMXULd0dxc

# Exmpressões Lambda - Simplificado
# * Funções "Anônimas" -> nome ruim pra uma função que você não precisa definir e depois usar, você define já usando direito.

# Ex:
# Digamos que você está avaliando o preço de um serviço e quer saber de imposto será cobrado sobre o serviço. O Imposto é correspondente a 30% do valor do produto,

def calcular_imposto(preco):
    return preco * 0.3

preco = 1000
print(calcular_imposto(preco))

    # Usando o lambda
calcular_imposto_lambda = lambda x: x * 0.3
print(calcular_imposto_lambda(preco))

# Tá, mas qual a diferença?
# Quando você aplica essa função dentro de outros métodos do Python, aí sim existem vantagem.
# Ex. temos agora uma lista de preços

precos = [100, 500, 200, 90]

impostos = list(map(lambda x:x * 0.3, precos)) # map(funcao, lista)
print(impostos)
