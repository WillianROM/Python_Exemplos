# https://www.youtube.com/watch?v=UW8Vf0dyEvs&list=PLmOO8X35BgB1rDGTZ1q4tzxCeK7RnFNqD&index=5&ab_channel=RonanVico
import pyautogui

#Automação do teclado
# Deixe um bloco de notas aberto para que o pyautogui possa fazer um ALT + TAB para ir para a janela do bloco de notas

#Aperta alt para baixo
pyautogui.keyDown('alt')
#Pressiona o TAB
pyautogui.press(['tab'])
#Solta a tecla alt
pyautogui.keyUp('alt')



#Digita o texto desejado
pyautogui.write("Fazendo um teste com a linguagem Python utilizando a biblioteca pyautogui")
