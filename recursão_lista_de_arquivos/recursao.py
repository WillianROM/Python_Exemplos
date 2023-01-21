# https://www.youtube.com/watch?v=fYSrdwRusOE

# Recursão em Python
# Desafio: Backup do sistema de Vendas

import os # Para percorrer pastas do computador

arquivos_extraidos = []

def pegar_arquivos_pastas(pasta):
    lista_arquivos = os.listdir(pasta) # Para listar os arquivos de um diretório
    # Se tiver txt e vendas no nome do arquivo, então pegue o nome do mÊs
    for arquivo in lista_arquivos:
        if ".txt" in arquivo and "Vendas" in arquivo:
            # Significa que eu quero pegar o nome do mês
            nome_mes = arquivo.split()[-1].replace(".txt","")
            arquivos_extraidos.append(nome_mes)
    # Caso contrário, não fazer nada
        elif ".txt" not in arquivo: # se é uma pasta
            pegar_arquivos_pastas(f'{pasta}/{arquivo}')


pegar_arquivos_pastas("Arquivos")
print(arquivos_extraidos)
