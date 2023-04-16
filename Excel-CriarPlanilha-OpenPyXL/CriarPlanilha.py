# https://www.youtube.com/watch?v=VOHwlUZlyuA&list=PLmOO8X35BgB1rDGTZ1q4tzxCeK7RnFNqD&ab_channel=RonanVico
# pip install openpyxl  
 
from openpyxl import Workbook
 
wb = Workbook() # Cria uma instância do objeto workbook

planilha = wb.worksheets[0] # Pega a primeira planilha do workbook, índice 0

# Preenche dados nas células:
planilha["A1"] = "MARIO"
planilha["A2"] = "LUIGI"

planilha.title = "Personagens" # Nome da aba

wb.save("C:\PYTHON\CriarPlanilhaExcel\MeuArquivo.xlsx") # Salva a planilha numa pasta
