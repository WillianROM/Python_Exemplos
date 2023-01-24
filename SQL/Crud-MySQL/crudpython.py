# Instale o drive do MySQL - pip install mysql-connector-python
import mysql.connector

    # Criar uma conexão
conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='123456',
    database='bdyoutube'
)

    # Criar um cursor
cursor = conexao.cursor()

""" Modelo
comando = ''
cursor.execute(comando)
conexao.commit() # se o comando edita o banco de dados tem que fazer conexao.commit()
resultado = cursor.fetchall() # ler o banco de dados
"""

# CREATE
"""
nome_produto = "NoBreak"
valor = 800

comando = f'INSERT INTO bdyoutube.vendas (nome_produto, valor) VALUES ("{nome_produto}", {valor})'
cursor.execute(comando)
conexao.commit() # se o comando edita o banco de dados tem que fazer conexao.commit()
"""


# READ
"""
comando = 'SELECT * FROM bdyoutube.vendas'
cursor.execute(comando)
resultado = cursor.fetchall() # ler o banco de dados
print(resultado)
"""


# UPDATE
"""
nome_produto = "NoBreak"
valor = 1000

comando = f'UPDATE bdyoutube.vendas SET valor = {valor} WHERE nome_produto = "{nome_produto}"'
cursor.execute(comando)
conexao.commit() # se o comando edita o banco de dados tem que fazer conexao.commit()
"""

# DELETE
"""
nome_produto = "NoBreak"

comando = f'DELETE FROM bdyoutube.vendas WHERE nome_produto = "{nome_produto}"'
cursor.execute(comando)
conexao.commit() # se o comando edita o banco de dados tem que fazer conexao.commit()
"""


    # Fechar o cursor e a conexão
cursor.close()
conexao.close()
