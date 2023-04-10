# Como dar join em planilhas excel e gerar gráficos usando Python como ferramenta de ETL
# https://www.youtube.com/watch?v=OziX7ZBjluI&list=PLmOO8X35BgB2wHXeAFGGEl75W1lXEDOIY&index=27&ab_channel=RonanVico

import pandas as pd 
import matplotlib.pyplot as plt # Para gerar gráfico
# plotly-express - Para fazer gráficos com dados da werb

arquivo_produtos = "PRODUTOS.xlsx"
arquivo_vendas = "VENDAS.xlsx"

# Lendo arquivox exceis e jogando na variável
df_produtos = pd.read_excel(arquivo_produtos,)
df_vendas = pd.read_excel(arquivo_vendas)

#Juntamos os 2 dataframes dos arquivos em 1 só dando Join
#DANDO PROCV, entenda como quiser pela coluna ID
df_total = df_produtos.merge(df_vendas,on="ID")

# Criar uma coluna de Total das vendas
df_total['TOTAL_VENDIDO'] = df_total['vendas_quantidade'] * df_total['Valor']

# Salvar os dados em uma nova planilha
df_total.to_excel('TOTAL_CONSOLIDADO.xlsx')

print(df_total)

#Gerar o gráfico
# kind='bar' - gráfico de barras
# df_total.plot(kind='bar') 

# kind='pie' - gráfico de pizza

df_total.TOTAL_VENDIDO.groupby(df_total.DESCRICAO).sum().plot(kind='pie') 

plt.show()


