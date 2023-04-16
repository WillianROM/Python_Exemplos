# https://www.youtube.com/watch?v=diLns814no0&list=PLmOO8X35BgB1rDGTZ1q4tzxCeK7RnFNqD&index=2&ab_channel=RonanVico
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

arquivo_excel_1 = "wb01.xlsx"
arquivo_excel_2 = "wb02.xlsx"

df_dia_1 = pd.read_excel(arquivo_excel_1,sheet_name="dia1")
df_dia_2 = pd.read_excel(arquivo_excel_1,sheet_name="dia2")
df_dia_3 = pd.read_excel(arquivo_excel_2,sheet_name="dia3")

# print(df_dia_1)
# print(df_dia_2)
# print(df_dia_3)


# CONSOLIDAR AS PLANILHAS E GERAR UMA NOVA PLANILHA

df_todas_as_planilhas_consolidadas = pd.concat([df_dia_1,df_dia_2,df_dia_3])
df_todas_as_planilhas_consolidadas.to_excel('CONSOLIDADO.xlsx')

# print(df_todas_as_planilhas_consolidadas)
# print(df_todas_as_planilhas_consolidadas["Vendedor"]) # Para imprimir apenas uma coluna específica


# Saber quanto cada vendedor vendeu
lucro_dos_vendodores = df_todas_as_planilhas_consolidadas.groupby(["Vendedor"]).sum() #  é como se fosse uma tabela dinâmica, para juntar os valores a partir de uma coluna
# print(lucro_dos_vendodores)


# Se eu quero imprimir somente as Unidades e Preço (Retirar a coluna Dia)
relatorio_enxuto = lucro_dos_vendodores.loc[:,"Unidades":"Preço"] # No loc[:,"Unidades":"Preço"], essa parte : é para pegar todas as linhas
#print(relatorio_enxuto)



# Gerar um gráfico
relatorio_enxuto.plot(kind='bar')

plt.show()
