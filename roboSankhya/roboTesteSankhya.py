from pywinauto_recorder.player import *
import pyautogui
import credentialSecrets


pyautogui.PAUSE = 2

pyautogui.press('win')
pyautogui.write('Sankhya')
pyautogui.press('enter')


with UIPath(u"Navegador Sankhya - [Sankhya]||Pane"):
	with UIPath(u"Navegador Sankhya - [Sankhya]||Document->||Pane->Sankhya Om||Document"):
		click(u"||Group")
		pyautogui.write(credentialSecrets.senha)
	
	with UIPath(u"Navegador Sankhya - [Sankhya]||Document->||Pane->Sankhya Om||Document->||Group"):
		click(u"Prosseguir||Button")
		
	with UIPath(u"Navegador Sankhya - [Sankhya]||Document->||Pane->Sankhya Om||Document->||Table->||Custom"):
		click(u"||DataItem#[0,0]")

	with UIPath(u"Navegador Sankhya - [Sankhya]||Document->||Pane->Sankhya Om||Document->||Table->||Custom->||DataItem->||Table->||Custom->Contabilidade||DataItem->||Table->||Custom->Contabilidade||DataItem"):
		click(u"Contabilidade||Text")

	with UIPath(u"Navegador Sankhya - [Sankhya]||Document->||Pane->Sankhya Om||Document"):
		click(u"Procurar em Contabilidade Fechar Contabilidade||Custom->||Custom->Arquivos||Custom->||Table->||Custom->Arquivos||DataItem->||Table->||Custom->Arquivos||DataItem->||Table->||Custom->Arquivos||DataItem->Arquivos||Text")


	lotesContabeis = pyautogui.locateCenterOnScreen(r'imagens\\lotesContabeis.png', confidence=0.7)

	while lotesContabeis == None:
		lotesContabeis = pyautogui.locateCenterOnScreen(r'imagens\\lotesContabeis.png', confidence=0.7)
		print("still haven't found the image")
	pyautogui.click(lotesContabeis.x,lotesContabeis.y)


	with UIPath(u"Navegador Sankhya - [Sankhya]||Document->||Pane->Sankhya Om||Document->||Pane->||Document->||Custom"):
		click(u"Digite o que você procura||Edit")
		pyautogui.write("Teste realizado com sucesso")
		send_keys(" \º/")
