# https://www.youtube.com/watch?v=paEIQHI2KkY&list=PLmOO8X35BgB1rDGTZ1q4tzxCeK7RnFNqD&index=6&ab_channel=RonanVico
import ctypes # importe para poder gerar a caixa de mensagem
import sys # para poder passar argumentos para as variáveis

# Variáveis da Caixa de Mensamgem:
#msg = "Olá, mundo"
#title = "teste"
#style = 5

msg = sys.argv[1]
title = sys.argv[2]
style = int(sys.argv[3])

ctypes.windll.user32.MessageBoxW(0, msg, title, style) # Para mostrar uma caixa de mensagem


## Styles:
## 0 : OK
## 1 : OK | Cancel
## 2 : Abort | Retry | Ignore
## 3 : Yes | No | Cancel
## 4 : Yes | No
## 5 : Retry | Cancel
## 6 : Cancel | Try Again | Continue
