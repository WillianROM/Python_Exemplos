# https://www.youtube.com/watch?v=6PACWNWEaJ8
# Tupla x Lista
tupla = (1,2,3,4,5,'texto') # Tuplas não permite alteração dos itens como uma constante - Não é mutável

lista = [1,2,3,4,5,'texto'] # As listas são mutáveis, como variáveis - Mutável

lista.append(6)

    #print(dir(tupla))


# Lista de Tuplas
cliente = ('Wilson','123.456.789-00','81.451.451/0001-03')
clientes = []
clientes.append(cliente)
print(clientes)

cliente = ('Mario','014.954.156-15','41.941.841/0001-45')
clientes.append(cliente)
print(clientes)

# Tuplas como Chaves de Dicionários
capitais = {
    ('Brasil','Rio de Janeiro'):'Rio de Janeiro',
    ('Brasil','São Paulo'):'São Paulo',
    ('Brasil','Paraná'):'Curitiba'
}


print(capitais.keys())
print(capitais.values())



# Métodos de Tuplas
tuplaMetodos = (1,2,3,4,5,12)
print(tuplaMetodos.index(3)) # Primeira posição de um item dentro da tupla, nesse caso o valor 3 está na posição 2, já que a base é Zero
print(tuplaMetodos.count(12)) # Para contar quantas vezes alguma valor aparece dentro da tupla

# Desafio: Criando um gerenciador de cadastro de materiais
lista_materiais = []
def cadastrarmateriais(nome, codigo, unidade, quantidade):
    tuplaDesafio = (nome, codigo, unidade, quantidade)
    lista_materiais.append(tuplaDesafio)
    return lista_materiais

def consultarmateriais(codigo):
    for material in lista_materiais:
        if material[1] == codigo:
            return print(material)
        else:
            pass


print(cadastrarmateriais('Borracha', 1, 'un',500))
print(consultarmateriais(1))