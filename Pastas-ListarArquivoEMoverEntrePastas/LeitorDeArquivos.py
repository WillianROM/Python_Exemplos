# https://www.youtube.com/watch?v=bgrRKmvP8As&list=PLmOO8X35BgB1rDGTZ1q4tzxCeK7RnFNqD&index=10&ab_channel=RonanVico

import os

# ir até a pasta que quero loopar
os.chdir("Pasta1") # Usar o prompt de comando para trocar a pasta

# Para cada Arquivo na Lista de arquivos no diretorio "List Dir"
for file in os.listdir(): 
    #Imprimir o arquivo
    print(file)
