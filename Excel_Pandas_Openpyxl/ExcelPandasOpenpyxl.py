# https://www.youtube.com/watch?v=IT7zPluDADk
"""
1. Pandas
    * Mais usada no geral
    * Trata o Excel como uma base de dados
    * Faz o que quiser com o arquivo
    * Pode desfazer a estrtura original do arquivo, caso queira editar
"""
# pip install pandas
import pandas as pd

tabela = pd.read_excel("Produtos.xlsx")

# atualizar o multiplicador
# tabela.loc[LINHA, COLUNA] = VALOR PARA COLOCAR NA CÉLULA
tabela.loc[tabela["Tipo"]=="Serviço", "Multiplicador Imposto"] = 1.5

# fazer a conta do Preço Base Reais
tabela["Preço Base Reais"] = tabela["Multiplicador Imposto"] * tabela["Preço Base Original"]

tabela.to_excel("ProdutosPandas.xlsx", index=False)

#==========================================================================================================================================

"""
2. Openpyxl
    * Trata o Excel como uma planilha mesmo que pode ter várias coisas
    * Edita "como se fosse um VBA"
    * Menos eficiente
    * Mantém mais estrutura original do arquivo, mas cuidado porque não necessariamente tudo, então tem que testar
"""
# pip install openpyxl
from openpyxl import Workbook, load_workbook

planilha = load_workbook("Produtos.xlsx")

aba_ativa = planilha.active

aba_ativa["A1"]

for celula in aba_ativa["C:C"]:
    if celula.value == "Serviço":
        linha = celula.row
        aba_ativa[f"D{linha}"] = 1.5

planilha.save("ProtudosOpenPy.xlsx")
