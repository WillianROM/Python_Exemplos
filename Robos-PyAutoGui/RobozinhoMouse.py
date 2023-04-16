# https://www.youtube.com/watch?v=UW8Vf0dyEvs&list=PLmOO8X35BgB1rDGTZ1q4tzxCeK7RnFNqD&index=6&ab_channel=RonanVico
import pyautogui

# Deixe o MSPaint aberto para que o pyautogui possa fazer um ALT + TAB para ir para a janela do MSPaint
#Aperta alt para baixo
pyautogui.keyDown('alt')
#Pressiona o TAB
pyautogui.press(['tab'])
#Solta a tecla alt
pyautogui.keyUp('alt')

#No Click dá para passar coordenadas X e Y ou uma imagem para localizar na tela para ser realizado o clique
pyautogui.click('circulo.png')

# Move o mouse para a área de desenho do MSPaint
pyautogui.move(xOffset=0,yOffset=200)

# Arrasta o mouse com clique na tela conforme as coordenadas
pyautogui.drag(xOffset=200,yOffset= 200,duration=5)

# Hotkey para fazer copia
pyautogui.hotkey('ctrl','c')