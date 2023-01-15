# CSV gerado no meu_robo_site_HTML_Table.py
import pandas as pd

# df - DataFrame (Estrutura dos Dados)
df1 = pd.read_csv('population_scraping_result.csv')
print(df1)

print(100 * "=")

df2 = pd.read_csv('population_scraping_result.csv', usecols=['Id', 'Valor'])
print(df2)

print(100 * "=")

df3 = pd.read_csv('population_scraping_result.csv', usecols=[0,1,4]) #Base ZERO
print(df3)

print(100 * "=")

print(df1.head(1)) #Mostra os dados da primeira linha

print(100 * "=")

# Agrupar por Descrição
groups_df = df1.groupby("Descrição")

for descricao, group in groups_df:
    print("----- {} -----".format(descricao))
    print(group)
    print("")

print(100 * "=")

