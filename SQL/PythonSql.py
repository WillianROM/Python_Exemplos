import server
# https://www.youtube.com/watch?v=Mdg1D-Kdmrw&ab_channel=HashtagPrograma%C3%A7%C3%A3o
# Passo 1: Baixar e instalar o SQL Server e SSMS
# Passo 2: Criar Banco de Dados, abrindo uma query e rodando:

# CREATE DABASE Nome_Banco_Dados

# Passo 3: Criar tabela, usando:

"""
USE Nome_Banco_Dados
CREATE TABLE Vendas(
    id_venda int,
    cliente varchar(50),
    produto varchar(50),
    data_venda date,
    preco decimal(6, 2),
    quantidade int
)
"""
# Passo 4: Adicionar 1 valor, exemplo:

"""
INSERT INTO Vendas(id_venda, cliente, produto, data_venda, preco, quantidade)
VALUES (1, 'João', 'Celular', '20/01/2023', 3000, 1)
"""
#####################################################################################
# No Python utilize a biblioteca pyodbc
# pip install pyodbc

import pyodbc

dados_conexao = (
    "Driver={SQL Server};"
    f"Server={server.serverName};" # Na empresa veja o link ou o IP, para estudo pesquise por hostname no CMD
    "Database=PythonSQL;"
)

conexao = pyodbc.connect(dados_conexao)
print("Conexão Bem Sucedida")

cursor = conexao.cursor()


id_venda = 4
cliente = 'Wilson'
produto = 'noBreak'
data_venda = '10/12/2022'
preco = 900
quantidade = 2

comando = f"""
INSERT INTO Vendas(id_venda, cliente, produto, data_venda, preco, quantidade)
VALUES ({id_venda}, '{cliente}', '{produto}', '{data_venda}', {preco}, {quantidade})
"""

cursor.execute(comando)
cursor.commit() # Só precisa se o comando edita algo do banco de dados, como adicionar, deletar, atualizar dados, criar nova tabela ...
