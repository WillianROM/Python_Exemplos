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
# print(arquivos_extraidos)


meses_sistema = ['ago2020', 'mai2020','ago2021','mai2021', 'abr2018','mai2018', 'set2018', 'set2019','mai2019', 'jul2017','mai2017' ,'dez2022', 'fev2022']

for mes in meses_sistema:
    if mes not in arquivos_extraidos:
        print(f"Mês {mes} está na lista dos meses_sistema, mas não está nos arquivos_extraídos.")
